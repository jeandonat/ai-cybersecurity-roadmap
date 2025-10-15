# AI-Driven Cybersecurity Roadmap
*A practical, hands-on path from securing your own box to a working mini-SOC — with AI where it helps most.*

## Projects (overview & deliverables)

1. **Secure Your Linux Workstation**  
   Harden SSH, firewall, fail2ban; weekly audit script.  
   *Tools:* `ufw`, `fail2ban`, `lynis`, `nmap`  
   **Deliverables:** `reports/`, `scripts/audit.sh`, hardening notes.

2. **Network Visibility & Monitoring**  
   Packet capture + anomaly spotting; alert on suspicious IPs.  
   *Tools:* Wireshark, `tcpdump`  
   **Deliverables:** capture samples, alert script, findings.

3. **Local Vulnerability Scanning**  
   Greenbone CE (OpenVAS) or Nessus Essentials; export **PDF/CSV**.  
   *Folder:* [`project3-local-vulnerability-scanning`](project3-local-vulnerability-scanning/)  
   **Deliverables:** `reports/YYYY-MM-DD_openvas_localhost.{pdf,csv}`, README, (optional) cron for weekly exports.

4. **Log Analysis & SIEM Setup**  
   Wazuh (manager + agent) or Splunk Free; dashboards for auth/FIM.  
   **Deliverables:** screenshots of failed-login alerts, FIM alerts, README.

5. **Mini SOC Simulation**  
   Wire vuln scanner + SIEM + monitors; simulate nmap/bruteforce; auto-actions.  
   **Deliverables:** playbooks/scripts, alert screenshots, runbook.

6. **Python for Security Automation**  
   Parsers, IP reputation, VirusTotal API enrichment; auto triage.  
   **Deliverables:** small `tools/` scripts with `README` and examples.

7. **AI-Enhanced Threat Detection**  
   Train simple models (e.g., scikit-learn) on logs; flag anomalies.  
   **Deliverables:** notebook(s), model artifacts, ROC/PR chart.

8. **Cloud & Container Security**  
   Run DVWA in Docker; scan with Trivy; runtime rules with Falco.  
   **Deliverables:** Trivy SARIF/HTML, Falco alerts, remediation notes.

9. **Final SOC Integration & Reporting**  
   Unified dashboard, KPIs, and **professional report**.  
   **Deliverables:** end-to-end diagram, executive summary PDF, recommendations.

---



