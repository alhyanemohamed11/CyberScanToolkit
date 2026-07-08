import socket
import ssl
from datetime import datetime


def parse_name(name_tuple):
    """
    Convert the nested tuple returned by getpeercert()
    into a normal Python dictionary.
    """

    result = {}

    for item in name_tuple:
        for key, value in item:
            result[key] = value

    return result


def get_ssl_certificate(hostname):

    try:

        context = ssl.create_default_context()

        with socket.create_connection((hostname, 443), timeout=5) as sock:

            with context.wrap_socket(
                sock,
                server_hostname=hostname
            ) as secure_socket:

                cert = secure_socket.getpeercert()

                subject = parse_name(cert["subject"])
                issuer = parse_name(cert["issuer"])

                valid_until = cert.get("notAfter")

                expiry_date = datetime.strptime(
                    valid_until,
                    "%b %d %H:%M:%S %Y %Z"
                )

                days_remaining = (expiry_date - datetime.utcnow()).days

                if days_remaining < 0:
                    status = "EXPIRED"
                elif days_remaining <= 30:
                    status = "EXPIRING SOON"
                else:
                    status = "VALID"

                return {
                    "subject": subject.get("commonName"),

                    "organization":
                        subject.get("organizationName"),

                    "issuer":
                        issuer.get("organizationName"),

                    "issuer_cn":
                        issuer.get("commonName"),

                    "version":
                        cert.get("version"),

                    "serial":
                        cert.get("serialNumber"),

                    "valid_from":
                        cert.get("notBefore"),

                    "valid_until":
                        cert.get("notAfter"),

                    "days_remaining":
                        days_remaining,

                    "status":
                        status,

                    "alt_names": [
                            value
                            for key, value in cert.get(
                                "subjectAltName",
                                []
                            )
                            if key == "DNS"
                    ]
                }

    except Exception:

        return None

