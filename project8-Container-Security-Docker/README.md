# Project 8 — Container Security (Falco → Wazuh + DVWA + Trivy)

## Recruiter proof (runtime detection → SIEM)
Falco detected suspicious container activity and it **landed as a Wazuh alert** (custom rule **100500**).

<img width="900" height="600" alt="01-alert-event-details" src="https://github.com/user-attachments/assets/30625209-a3f0-4b5a-97fc-7d9dd55fb55b" />

---

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
- Exec summary: `step8-dvwa-trivy-vuln-scanning/reports/00-trivy-exec-summary.txt`
- HIGH/CRITICAL: `step8-dvwa-trivy-vuln-scanning/reports/01-trivy-high-critical.txt`
- Full JSON: `step8-dvwa-trivy-vuln-scanning/reports/02-trivy-report.json`

### Mitigations (real-world pattern)
Even in a lab, the correct operational pattern is:
- Prefer images built on **supported base OS versions** (or distroless where appropriate).
- Rebuild regularly and pin versions; treat EOL base images as a risk signal.
- Keep DVWA **local-only / segmented** and never expose it publicly.

---

## Lab setup
- **Wazuh Manager (VM):** `wazuh-server`
- **Wazuh Agent (host):** `ubuntu-docker-host` (agent id **002**)
- **Falco:** `falco-modern-bpf.service` writing JSON to `/var/log/falco.json`
- **Trigger:** `docker run --rm -it alpine sh`

## Evidence (screenshots)
1. **Alert details (Threat Hunting):** agent 002 + rule.id 100500 + level 12 + MITRE T1059  
   - `step8-falco-runtime-detection/screenshots/01-alert-event-details.png`

2. **Custom rule (Rules view):** correlation rule definition + MITRE mapping  
   - `step8-falco-runtime-detection/screenshots/02-rule-100500.png`

3. **DVWA running (docker ps + UI):** local-only exposure on 127.0.0.1:8081  
   - `step8-dvwa-trivy-vuln-scanning/screenshots/01-docker-ps-dvwa.png`
   - `step8-dvwa-trivy-vuln-scanning/screenshots/03-dvwa-home-logged-in.png`

## Configuration

### Falco JSON output
Falco writes JSON events to:
- `/var/log/falco.json`

### Wazuh agent ingestion (ubuntu-docker-host)
Configured `ossec.conf` to ingest Falco JSON:
