
# Step 6 — Python for Security Automation

This project contains a collection of Python tools for:
- Log parsing
- IP reputation checks
- Malware hash lookup (VirusTotal)
- Automatic event triage
- JSON reporting

The scripts are lightweight and designed for Tier-1 SOC automation,
mini-SOC pipelines, or integration into Wazuh custom commands.

## Tools Included

### 1) ip_reputation_checker.py
Checks IP addresses against:
- VirusTotal IP API
- AbuseIPDB (optional)
- Custom local blocklist

### 2) vt_hash_lookup.py
Looks up file hashes (MD5/SHA1/SHA256) in VirusTotal.

### 3) log_parser.py
Parses common logs:
- auth.log
- syslog
- SSH failures
- Suspicious commands

### 4) auto_triage.py
Takes logs + IPs + hashes and produces:
- Severity score (0–10)
- Recommended action
- JSON output

## Requirements
