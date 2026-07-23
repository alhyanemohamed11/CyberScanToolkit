import json
from pathlib import Path
from datetime import datetime


def save_json_report(scan_result):

    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = (
        scan_result["target"].replace(".", "_")
        + "_"
        + timestamp
        + ".json"
    )

    report_path = reports_dir / filename

    with open(report_path, "w", encoding="utf-8") as file:
        json.dump(scan_result, file, indent=4)

    return report_path