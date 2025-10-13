
# Project 1 — Linux Hardening
Part of my [AI-Driven Cybersecurity Roadmap](../README.md)  
Goal: secure a local Linux workstation by auditing, reducing services, and verifying firewall & intrusion protection.

## Objective
Secure my Linux workstation by configuring SSH, UFW, and Fail2Ban, and auditing open ports.

## Tools Used
- UFW
- SSH
- Fail2Ban
- nmap
- Bash

## Steps
1. Scanned open ports with `nmap -sS localhost`
2. Disabled root SSH and password login
3. Configured UFW rules (deny incoming, allow outgoing, allow SSH)
4. Installed and verified Fail2Ban
5. Created `security_audit.sh` to automate weekly audits

## Results
- [x] Firewall active
- [x] SSH locked down
- [x] Intrusion prevention running

## Evidence
- `port_scan_nmap.txt`
- `system_audit_report.txt`
- Screenshots in `/screenshots`

## Lessons Learned
Short note about what you discovered or improved.
