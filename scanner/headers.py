import requests

SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy"
]


def analyze_security_headers(hostname):
    """
    Analyze HTTP security headers of a website.
    """

    url = f"https://{hostname}"

    try:
        response = requests.get(
            url,
            timeout=5,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        results = {}

        # Check every security header
        for header in SECURITY_HEADERS:

            value = response.headers.get(header)

            results[header] = {
                "present": value is not None,
                "value": value
            }

        # Count how many headers are present
        score = sum(
            info["present"] for info in results.values()
        )

        analysis = {
            "url": response.url,
            "status_code": response.status_code,
            "server": response.headers.get("Server", "Unknown"),
            "headers": results,
            "score": score,
            "total": len(SECURITY_HEADERS)
        }

        return analysis

    except requests.exceptions.Timeout:
        print("[ERROR] Connection timed out.")
        return None

    except requests.exceptions.ConnectionError:
        print("[ERROR] Could not connect to the server.")
        return None

    except requests.exceptions.SSLError:
        print("[ERROR] SSL certificate verification failed.")
        return None

    except requests.exceptions.RequestException as error:
        print(f"[ERROR] {error}")
        return None