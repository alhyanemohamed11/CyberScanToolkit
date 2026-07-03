import socket

COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 8080]

PORT_NAMES = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-Alt",
}


def scan_ports(ip):

    open_ports = []

    total_ports = len(COMMON_PORTS)

    for index, port in enumerate(COMMON_PORTS, start=1):

        print(
            f"\r[{index}/{total_ports}] Checking port {port}...",
            end="",
            flush=True
        )

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

            sock.settimeout(1)

            result = sock.connect_ex((ip, port))

            if result == 0:

                open_ports.append({
                    "port": port,
                    "service": PORT_NAMES.get(port, "Unknown"),
                    "banner": None
                })

    print()

    return open_ports