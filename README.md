# 🔍 CyberScan Toolkit

CyberScan Toolkit is a modular Python-based network reconnaissance and security assessment tool.

It analyzes a target host by performing:

- DNS resolution
- TCP port scanning
- Banner grabbing
- SSL/TLS certificate inspection
- HTTP security header analysis
- Security assessment

The toolkit also generates professional **JSON** and **HTML** reports summarizing the scan results.

## ✨ Features

- 🌐 DNS hostname resolution
- 🔍 TCP port scanning
- 📡 Service detection
- 🏷️ Banner grabbing
- 🔒 SSL/TLS certificate analysis
- 🛡️ HTTP security header analysis
- 📊 Automated security assessment
- 📄 JSON report generation
- 🌍 HTML report generation
- 🎨 Professional terminal interface


## 📁 Project Structure

```text
CyberScanToolkit/
│
├── cyberscan.py                 # Main application
├── requirements.txt             # Project dependencies
├── README.md                    # Project documentation
│
├── scanner/                     # Scanning modules
│   ├── dns_lookup.py
│   ├── port_scanner.py
│   ├── banner.py
│   ├── ssl_checker.py
│   ├── headers.py
│   └── security_assessment.py
│
├── report/                      # Report generators
│   ├── json_report.py
│   └── html_report.py
│
├── reports/                     # Generated reports
│
└── utils/                       # Utility modules
    ├── colors.py
    └── display.py
```
## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/CyberScanToolkit.git
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Go to the project directory

```bash
cd CyberScanToolkit
```

### 3. Create a virtual environment

Linux/macOS:

```bash
python3 -m venv .venv
```

### 4. Activate the virtual environment

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

Windows (Command Prompt):

```cmd
.venv\Scripts\activate.bat
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```
## ▶️ Usage

Run the scanner:

```bash
python3 cyberscan.py
```

When prompted, enter the target hostname:

```text
Enter a hostname: github.com
```

The toolkit will perform the following steps:

1. Resolve the hostname to an IP address.
2. Scan common TCP ports.
3. Detect running services.
4. Grab service banners.
5. Analyze the SSL/TLS certificate (if HTTPS is available).
6. Check HTTP security headers.
7. Generate a security assessment.
8. Save the results as JSON and HTML reports.

### Example Output

```text
============================================================
CyberScan Toolkit
============================================================

Target      : github.com
IP Address  : 140.82.114.4

PORT SCAN RESULTS

PORT    SERVICE    BANNER

22      SSH        SSH-2.0-...
80      HTTP       HTTP/1.1 301 Moved Permanently
443     HTTPS      No banner

SSL CERTIFICATE

Status          : VALID
Issuer          : Sectigo Limited

HTTP SECURITY HEADERS

Security Score  : 5/6 (83%)

SECURITY ASSESSMENT

Overall Score   : 8/10
Rating          : Good

✓ Scan completed successfully.
```

### Generated Reports

After each scan, CyberScan Toolkit automatically creates two reports inside the `reports/` directory:

```text
reports/

github_com_20260731_145210.json

github_com_20260731_145210.html
```

- **JSON Report** — Machine-readable output for automation and further processing.
- **HTML Report** — Human-readable report that can be opened in any web browser.