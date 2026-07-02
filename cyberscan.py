from scanner.dns_lookup import resolve_hostname
from scanner.port_scanner import scan_ports, PORT_NAMES

def main():
    target = input("Enter a hostname: ").strip()
    if not target:
        print("[-] No hostname entered.")
        return

    ip = resolve_hostname(target)
    if ip is None:
        print("[-] Could not resolve hostname.")
        return

    print(f"[+] Hostname : {target}")
    print(f"[+] IP Address: {ip}")
    print("\nScanning common TCP ports...\n")

    open_ports = scan_ports(ip)

    if open_ports:
        for port in open_ports:
            name = PORT_NAMES.get(port, "Unknown")
            print(f"[OPEN] Port {port} ({name})")
    else:
        print("No open common ports found.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[-] Interrupted by user.")