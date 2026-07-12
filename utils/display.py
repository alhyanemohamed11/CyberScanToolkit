from utils.colors import *


LINE = "=" * 80
SUBLINE = "-" * 80


def print_header(target, ip):

    print("\n" + CYAN + BOLD + LINE + RESET)
    print(CYAN + BOLD + "CyberScan Toolkit".center(80) + RESET)
    print(CYAN + BOLD + LINE + RESET)

    print(f"Target      : {target}")
    print(f"IP Address  : {ip}")

    print(CYAN + LINE + RESET)


def print_results(open_ports):

    print("\n" + BOLD + "PORT SCAN RESULTS" + RESET)
    print(SUBLINE)

    print(
        f"{'PORT':<10}"
        f"{'SERVICE':<15}"
        f"{'BANNER'}"
    )

    print(SUBLINE)

    for port in open_ports:

        banner = port.get("banner")

        if banner:
            banner = banner.splitlines()[0]
            if len(banner) > 45:
                banner = banner[:45] + "..."
        else:
            banner = "No banner"

        print(
            f"{GREEN}{port['port']:<10}{RESET}"
            f"{port['service']:<15}"
            f"{banner}"
        )

    print(SUBLINE)


def print_ssl_info(info):

    if info is None:
        return

    print("\n" + BOLD + "SSL CERTIFICATE" + RESET)
    print(SUBLINE)

    print(f"Subject         : {info['subject']}")
    print(f"Issuer          : {info['issuer']}")
    print(f"Valid Until     : {info['valid_until']}")
    print(f"Days Remaining  : {info['days_remaining']}")

    status = info["status"]

    if status.upper() == "VALID":
        status = GREEN + status + RESET
    else:
        status = RED + status + RESET

    print(f"Status          : {status}")

    print(SUBLINE)


def display_header_analysis(analysis):

    if analysis is None:
        return

    print("\n" + BOLD + "HTTP SECURITY HEADERS" + RESET)
    print(SUBLINE)

    print(f"URL          : {analysis['url']}")
    print(f"Status Code  : {analysis['status_code']}")
    print(f"Web Server   : {analysis['server']}")

    print()

    print(
        f"{'HEADER':<35}"
        f"{'STATUS':<12}"
        f"VALUE"
    )

    print(SUBLINE)

    for header, info in analysis["headers"].items():

        if info["present"]:
            status = GREEN + "Present" + RESET
        else:
            status = RED + "Missing" + RESET

        value = info["value"]

        if value is None:
            value = "-"

        elif len(value) > 40:
            value = value[:40] + "..."

        print(
            f"{header:<35}"
            f"{status:<20}"
            f"{value}"
        )

    print(SUBLINE)

    score = analysis["score"]
    total = analysis["total"]

    percent = (score / total) * 100

    if percent >= 80:
        color = GREEN
    elif percent >= 50:
        color = YELLOW
    else:
        color = RED

    print(
        color +
        f"Security Score : {score}/{total} ({percent:.0f}%)"
        + RESET
    )

    print(CYAN + LINE + RESET)