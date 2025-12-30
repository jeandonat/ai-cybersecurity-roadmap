<<<<<<< Updated upstream
# Step 8 — Falco Runtime Detection → Wazuh Alert (MITRE T1059)

⭐ Featured: Recruiter highlights

**Interactive shell spawned inside a container → detected by Falco → ingested by Wazuh agent (002) → correlated by custom rule `100500` (level 12) → visible in Wazuh Dashboard with MITRE mapping (`T1059`).**
➡️ **Write-up / files:** [Falco runtime detection]



<img width="900" height="600" alt="01-alert-event-details" src="https://github.com/user-attachments/assets/30625209-a3f0-4b5a-97fc-7d9dd55fb55b" />

## Goal
Detect interactive shells spawned inside containers (Falco) and surface them as correlated alerts in Wazuh Dashboard,
mapped to MITRE ATT&CK.
=======
# Project 8 — Container Security (Falco → Wazuh + DVWA + Trivy)

## Recruiter proof (runtime detection → SIEM)
Falco detected suspicious container activity and it **landed as a Wazuh alert** (custom rule **100500**).


---
<img width="900" height="600" alt="01-alert-event-details" src="https://github.com/user-attachments/assets/30625209-a3f0-4b5a-97fc-7d9dd55fb55b" />

This project demonstrates **two complementary layers** of container security in a lab:

1) **Runtime detection (behavioral):** Falco detects suspicious container activity and forwards it into Wazuh.
2) **Vulnerability scanning (pre-runtime):** Trivy scans the DVWA container image and produces a vulnerability report.


## Step 8A — Falco runtime detection → Wazuh (recruiter proof)
**What it proves:** A container runtime event is detected by Falco and becomes a searchable Wazuh alert.

- Evidence (screenshots): `step8-falco-runtime-detection/screenshots/`
- Key config snippets: `step8-falco-runtime-detection/configs/`
- Reproduce commands: `step8-falco-runtime-detection/commands/commands-reproduce.txt`

---

## Step 8B — DVWA + Trivy vulnerability scanning
**What it proves:** A deliberately vulnerable container app (DVWA) is running locally, and its image is scanned with Trivy.

- DVWA (local-only): `127.0.0.1:8081 → container:80`
- Evidence (screenshots): `step8-dvwa-trivy-vuln-scanning/screenshots/`
- Trivy reports: `step8-dvwa-trivy-vuln-scanning/reports/`
- Reproduce commands: `step8-dvwa-trivy-vuln-scanning/commands/commands-reproduce.txt`

### Findings (short)
- Trivy detects the DVWA image OS as **Debian 9.5** and warns it is **end-of-life (EOL)** (security updates may no longer be provided).
- This increases the likelihood of **unpatched known vulnerabilities** in base packages.

**Evidence:**
- Exec summary: `reports/00-trivy-exec-summary.txt`
- HIGH/CRITICAL: `reports/01-trivy-high-critical.txt`
- Full JSON: `reports/02-trivy-report.json`

### Mitigations (real-world pattern)
Even in a lab, the correct operational pattern is:
- Prefer images built on **supported base OS versions** (or distroless where appropriate).
- Rebuild regularly and pin versions; treat EOL base images as a risk signal.
- Keep DVWA **local-only / segmented** and never expose it publicly.

>>>>>>> Stashed changes

## Lab setup
- **Wazuh Manager (VM):** `wazuh-server`
- **Wazuh Agent (host):** `ubuntu-docker-host` (agent id **002**)
- **Falco:** `falco-modern-bpf.service` writing JSON to `/var/log/falco.json`
- **Trigger:** `docker run --rm -it alpine sh`

## Evidence (screenshots)
1. **Alert details (Threat Hunting):** agent 002 + rule.id 100500 + level 12 + MITRE T1059  
   ![Falco alert in Wazuh]

2. **Custom rule (Rules view):** correlation rule definition + MITRE mapping  
   ![Wazuh rule 100500]

## Configuration

### Falco JSON output
Falco writes JSON events to:
- `/var/log/falco.json`

### Wazuh agent ingestion (ubuntu-docker-host)
Configured `ossec.conf` to ingest Falco JSON:

<<<<<<< Updated upstream
```xml
<localfile>
  <log_format>json</log_format>
  <location>/var/log/falco.json</location>
</localfile>
=======

>>>>>>> Stashed changes
