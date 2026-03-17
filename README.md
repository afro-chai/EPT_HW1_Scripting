# EPT Week 1 – Pentest Engagement Folder Structure

This script creates a standard folder structure for managing data during a pentesting engagement. Run it from the directory where you want the structure to appear (e.g., your engagement root).

## Requirements

- Python 3.6+

## Usage

From a terminal, `cd` to the directory that should contain the engagement folders, then run:

```bash
python engagement_setup.py
```

Or from anywhere, specifying the base directory:

```bash
python engagement_setup.py --base-dir /path/to/engagement
```

**Dry run** (print what would be created without creating it):

```bash
python engagement_setup.py --dry-run
```

## Generated structure

- **Documentation**
  - Customer Info
  - Reports
- **Findings**
  - External, Internal, Phishing
- **Data**
  - Database
  - Phishing (Templates, Payloads)
  - Network Mapping (External/Internal: Nmap, Eyewitness)
  - Penetration Test
  - Vulnerability Scanning (External/Internal: Nessus)
  - Web App (Burp, Nikto)

The script is idempotent: safe to run multiple times; existing directories are left unchanged.
