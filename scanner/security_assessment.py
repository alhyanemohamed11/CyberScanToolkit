def assess_security(scan_result):

    assessment = {

        "score": 0,
        "max_score": 10,
        "rating": "",
        "findings": [],
        "warnings": [],
        "recommendations": []

    }

    # -----------------------------------
    # SSL Assessment
    # -----------------------------------

    ssl = scan_result.get("ssl")

    if ssl:

        if ssl["status"] == "VALID":

            assessment["score"] += 2

            assessment["findings"].append(
                "SSL certificate is valid."
            )

        else:

            assessment["warnings"].append(
                "SSL certificate is not valid."
            )

            assessment["recommendations"].append(
                "Renew or replace the SSL certificate."
            )

    else:

        assessment["warnings"].append(
            "HTTPS is not available."
        )

        assessment["recommendations"].append(
            "Enable HTTPS to secure communications."
        )

    # -----------------------------------
    # HTTP Security Headers
    # -----------------------------------

    headers = scan_result.get("headers")

    if headers:

        for header, info in headers["headers"].items():

            if info["present"]:

                assessment["score"] += 1

                assessment["findings"].append(
                    f"{header} is configured."
                )

            else:

                assessment["warnings"].append(
                    f"{header} is missing."
                )

                assessment["recommendations"].append(
                    f"Configure the {header} HTTP header."
                )

    # -----------------------------------
    # Open Ports
    # -----------------------------------

    dangerous_ports = {

        21: (
            "FTP service detected.",
            "Use SFTP or FTPS if possible."
        ),

        23: (
            "Telnet service detected.",
            "Replace Telnet with SSH."
        ),

        3389: (
            "RDP service exposed.",
            "Restrict RDP access using a firewall or VPN."
        )

    }

    for port in scan_result["ports"]:

        port_number = port["port"]

        if port_number in dangerous_ports:

            warning, recommendation = dangerous_ports[port_number]

            assessment["warnings"].append(warning)

            assessment["recommendations"].append(recommendation)

    # -----------------------------------
    # Rating
    # -----------------------------------

    score = assessment["score"]

    if score >= 9:

        assessment["rating"] = "Excellent"

    elif score >= 7:

        assessment["rating"] = "Good"

    elif score >= 4:

        assessment["rating"] = "Fair"

    else:

        assessment["rating"] = "Poor"

    return assessment