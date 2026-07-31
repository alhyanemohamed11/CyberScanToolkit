from scanner.dns_lookup import resolve_hostname
from scanner.port_scanner import scan_ports
from scanner.banner import grab_banner
from scanner.ssl_checker import get_ssl_certificate
from scanner.headers import analyze_security_headers
from scanner.security_assessment import assess_security

from report.json_report import save_json_report
from report.html_report import save_html_report

from utils.display import (
    print_header,
    print_results,
    print_ssl_info,
    display_header_analysis,
    display_security_assessment
)

from utils.colors import *


def main():

    target = input("Enter a hostname: ").strip()

    if not target:
        print(RED + "[-] No hostname entered." + RESET)
        return

    # -----------------------------
    # DNS Resolution
    # -----------------------------

    ip = resolve_hostname(target)

    if ip is None:
        print(RED + "[-] Could not resolve hostname." + RESET)
        return

    print_header(target, ip)

    print("\nScanning common TCP ports...\n")

    # -----------------------------
    # Port Scan
    # -----------------------------

    open_ports = scan_ports(ip)

    if not open_ports:
        print(RED + "[-] No open ports found." + RESET)
        return

    ssl_info = None
    header_analysis = None

    # -----------------------------
    # Banner Grabbing
    # SSL Analysis
    # HTTP Header Analysis
    # -----------------------------

    for port in open_ports:

        port["banner"] = grab_banner(
            ip,
            port["port"]
        )

        if port["port"] == 443:

            ssl_info = get_ssl_certificate(target)

            header_analysis = analyze_security_headers(target)

    # -----------------------------
    # Display Scan Results
    # -----------------------------

    print_results(open_ports)

    if ssl_info:
        print_ssl_info(ssl_info)

    if header_analysis:
        display_header_analysis(header_analysis)

    # -----------------------------
    # Build Scan Result
    # -----------------------------

    scan_result = {

        "target": target,

        "ip": ip,

        "ports": open_ports,

        "ssl": ssl_info,

        "headers": header_analysis

    }

    # -----------------------------
    # Security Assessment
    # -----------------------------

    assessment = assess_security(scan_result)

    scan_result["assessment"] = assessment

    display_security_assessment(assessment)

    # -----------------------------
    # Generate Reports
    # -----------------------------

    json_report = save_json_report(scan_result)

    html_report = save_html_report(scan_result)

    # -----------------------------
    # Summary
    # -----------------------------

    print("\n" + CYAN + BOLD + "=" * 80 + RESET)
    print(CYAN + BOLD + "SCAN SUMMARY".center(80) + RESET)
    print(CYAN + BOLD + "=" * 80 + RESET)

    print(f"Target            : {target}")
    print(f"IP Address        : {ip}")
    print(f"Open Ports        : {len(open_ports)}")

    if ssl_info:
        print(f"HTTPS             : {GREEN}Available{RESET}")
        print(f"Certificate       : {ssl_info['status']}")
    else:
        print(f"HTTPS             : {RED}Not Available{RESET}")

    if header_analysis:

        score = header_analysis["score"]
        total = header_analysis["total"]

        percentage = (score / total) * 100

        if percentage >= 80:
            color = GREEN
        elif percentage >= 50:
            color = YELLOW
        else:
            color = RED

        print(
            f"Security Headers  : "
            f"{color}{score}/{total} ({percentage:.0f}%){RESET}"
        )

    print(
        f"Security Rating   : "
        f"{GREEN if assessment['rating'] in ['Excellent', 'Good'] else YELLOW}{assessment['rating']}{RESET}"
    )

    print(
        f"Security Score    : "
        f"{assessment['score']}/{assessment['max_score']}"
    )

    print(f"JSON Report       : {json_report}")
    print(f"HTML Report       : {html_report}")

    print(CYAN + "=" * 80 + RESET)

    print()

    print(GREEN + "✓ Scan completed successfully." + RESET)
    print(GREEN + f"✓ JSON report saved to : {json_report}" + RESET)
    print(GREEN + f"✓ HTML report saved to : {html_report}" + RESET)

    print()


if __name__ == "__main__":

    try:
        main()

    except KeyboardInterrupt:
        print("\n" + RED + "[-] Scan interrupted by user." + RESET)