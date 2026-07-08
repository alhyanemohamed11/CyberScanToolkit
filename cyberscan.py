from scanner.dns_lookup import resolve_hostname
from scanner.port_scanner import scan_ports
from scanner.banner import grab_banner
from scanner.ssl_checker import get_ssl_certificate


def print_header(target, ip):

    print("\n" + "=" * 90)
    print(" " * 30 + "CyberScan Toolkit")
    print("=" * 90)

    print(f"Target      : {target}")
    print(f"IP Address  : {ip}")

    print("=" * 90)


def print_results(open_ports):

    print("\nScan Results")

    print("=" * 90)

    print(f"{'PORT':<10}{'SERVICE':<15}{'BANNER'}")

    print("-" * 90)

    for port in open_ports:

        banner = port["banner"]

        if banner:
            banner = banner.splitlines()[0][:60]
        else:
            banner = "No banner"

        print(
            f"{port['port']:<10}"
            f"{port['service']:<15}"
            f"{banner}"
        )

    print("=" * 90)


def print_ssl_info(info):

    if info is None:
        return

    print("\nSSL Certificate Information")

    print("=" * 90)

    print(f"Subject           : {info['subject']}")
    print(f"Organization      : {info['organization']}")
    print(f"Issuer            : {info['issuer']}")
    print(f"Issuer CN         : {info['issuer_cn']}")
    print(f"Version           : {info['version']}")
    print(f"Serial Number     : {info['serial']}")
    print(f"Valid From        : {info['valid_from']}")
    print(f"Valid Until       : {info['valid_until']}")
    print(f"Days Remaining    : {info['days_remaining']}")
    print(f"Certificate Status: {info['status']}")

    if info["alt_names"]:

        print("\nAlternative Names")

        print("-" * 90)

        for domain in info["alt_names"]:
            print(f" - {domain}")

    print("=" * 90)


def main():

    target = input("Enter a hostname: ").strip()

    if not target:

        print("[-] No hostname entered.")
        return

    ip = resolve_hostname(target)

    if ip is None:

        print("[-] Could not resolve hostname.")
        return

    print_header(target, ip)

    print("\nScanning common TCP ports...\n")

    open_ports = scan_ports(ip)

    if not open_ports:

        print("\nNo open ports found.")
        return

    ssl_info = None

    for port in open_ports:

        port["banner"] = grab_banner(
            ip,
            port["port"]
        )

        if port["port"] == 443:

            ssl_info = get_ssl_certificate(target)

    print_results(open_ports)

    print_ssl_info(ssl_info)

    print(f"\nOpen Ports Found : {len(open_ports)}")

    print("\nScan Finished.\n")


if __name__ == "__main__":

    try:

        main()

    except KeyboardInterrupt:

        print("\nInterrupted by user.")