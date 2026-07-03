from scanner.dns_lookup import resolve_hostname
from scanner.port_scanner import scan_ports
from scanner.banner import grab_banner


def print_header(target, ip):
    print("\n" + "=" * 80)
    print(" " * 28 + "CyberScan Toolkit")
    print("=" * 80)
    print(f"Target      : {target}")
    print(f"IP Address  : {ip}")
    print("=" * 80)


def print_results(open_ports):
    print("\nScan Results")
    print("=" * 100)
    print(f"{'PORT':<10}{'SERVICE':<15}{'BANNER'}")
    print("-" * 100)

    for port_info in open_ports:

        banner = port_info["banner"]

        if banner:
            # Display only the first line and limit its length
            banner = banner.splitlines()[0][:65]
        else:
            banner = "No banner"

        print(
            f"{port_info['port']:<10}"
            f"{port_info['service']:<15}"
            f"{banner}"
        )

    print("=" * 100)
    print(f"Open Ports : {len(open_ports)}")
    print("Scan Finished.\n")


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
        print("\n[-] No open common ports found.")
        return

    # Grab the banner for each open port
    for port_info in open_ports:

        port_info["banner"] = grab_banner(
            ip,
            port_info["port"]
        )

    print_results(open_ports)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[-] Scan interrupted by user.")