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