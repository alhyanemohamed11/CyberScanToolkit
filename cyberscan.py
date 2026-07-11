from scanner.dns_lookup import resolve_hostname
from scanner.port_scanner import scan_ports
from scanner.banner import grab_banner
from scanner.ssl_checker import get_ssl_certificate


from utils.display import (
    print_header,
    print_results,
    print_ssl_info
)

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