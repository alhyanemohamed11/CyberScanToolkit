from scanner.dns_lookup import resolve_hostname
from scanner.port_scanner import scan_ports
from scanner.banner import grab_banner
from scanner.ssl_checker import get_ssl_certificate
from scanner.headers import analyze_security_headers

from report.json_report import save_json_report

from utils.display import (
    print_header,
    print_results,
    print_ssl_info,
    display_header_analysis
)

from utils.colors import *


def main():

    target = input("Enter a hostname: ").strip()

    if not target:
        print(RED + "[-] No hostname entered." + RESET)
        return

    # Resolve hostname
    ip = resolve_hostname(target)

    if ip is None:
        print(RED + "[-] Could not resolve hostname." + RESET)
        return

    print_header(target, ip)

    print("\nScanning common TCP ports...\n")

    # Scan ports
    open_ports = scan_ports(ip)

    if not open_ports:
        print(RED + "[-] No open ports found." + RESET)
        return

    ssl_info = None
    header_analysis = None

    # Banner Grabbing + HTTPS Analysis
    for port in open_ports:

        port["banner"] = grab_banner(
            ip,
            port["port"]
        )

        if port["port"] == 443:

            ssl_info = get_ssl_certificate(target)

            header_analysis = analyze_security_headers(target)

    # Display scan results
    print_results(open_ports)

    if ssl_info:
        print_ssl_info(ssl_info)

    if header_analysis:
        display_header_analysis(header_analysis)

    # --------------------------------------------------
    # Create one dictionary containing the entire scan
    # --------------------------------------------------

    scan_result = {

        "target": target,

        "ip": ip,

        "ports": open_ports,

        "ssl": ssl_info,

        "headers": header_analysis

    }

    # Save JSON report

    report_path = save_json_report(scan_result)

    # --------------------------------------------------
    # Summary
    # --------------------------------------------------

    print("\n" + CYAN + BOLD + "=" * 80 + RESET)
    print(CYAN + BOLD + "SCAN SUMMARY".center(80) + RESET)
    print(CYAN + BOLD + "=" * 80 + RESET)

    print(f"Target           : {target}")
    print(f"IP Address       : {ip}")
    print(f"Open Ports       : {len(open_ports)}")

    if ssl_info:
        print(f"HTTPS            : {GREEN}Available{RESET}")
        print(f"Certificate      : {ssl_info['status']}")
    else:
        print(f"HTTPS            : {RED}Not Available{RESET}")

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
            f"Security Headers : "
            f"{color}{score}/{total} ({percentage:.0f}%){RESET}"
        )

    print(f"JSON Report      : {report_path}")

    print(CYAN + "=" * 80 + RESET)

    print()

    print(GREEN + "✓ Scan completed successfully." + RESET)

    print(GREEN + f"✓ JSON report saved to: {report_path}" + RESET)

    print()


if __name__ == "__main__":

    try:
        main()

    except KeyboardInterrupt:

        print("\n" + RED + "[-] Scan interrupted by user." + RESET)