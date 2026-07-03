import socket


def grab_banner(ip, port):

    try:

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

            sock.settimeout(2)

            sock.connect((ip, port))

            if port == 80:

                request = (
                    "GET / HTTP/1.1\r\n"
                    f"Host: {ip}\r\n"
                    "Connection: close\r\n\r\n"
                )

                sock.send(request.encode())

            banner = sock.recv(1024)

            return banner.decode(errors="ignore").strip()

    except (socket.timeout, ConnectionError, OSError):

        return None