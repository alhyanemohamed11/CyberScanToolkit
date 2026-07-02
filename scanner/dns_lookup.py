import socket


def resolve_hostname(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    
    except socket.gaierror as e:
        print(f"[-] DNS error: {e}")
        return None