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