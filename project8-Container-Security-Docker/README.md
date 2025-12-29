# Step 8 — Falco Runtime Detection → Wazuh Alert (MITRE T1059)

⭐ Featured: Recruiter highlights

Falco → Wazuh alert (MITRE T1059) (Container shell detection, custom Wazuh rule 100500)
→ project8-container-security/falco-runtime-detection/


<img width="1717" height="1289" alt="01-alert-event-details" src="https://github.com/user-attachments/assets/30625209-a3f0-4b5a-97fc-7d9dd55fb55b" />

## Goal
Detect interactive shells spawned inside containers (Falco) and surface them as correlated alerts in Wazuh Dashboard,
mapped to MITRE ATT&CK.

## Lab setup
- **Wazuh Manager (VM):** `wazuh-server`
- **Wazuh Agent (host):** `ubuntu-docker-host` (agent id **002**)
- **Falco:** `falco-modern-bpf.service` writing JSON to `/var/log/falco.json`
- **Trigger:** `docker run --rm -it alpine sh`

## Evidence (screenshots)
1. **Alert details (Threat Hunting):** agent 002 + rule.id 100500 + level 12 + MITRE T1059  
   ![Falco alert in Wazuh](screenshots/01-alert-event-details.png)

2. **Custom rule (Rules view):** correlation rule definition + MITRE mapping  
   ![Wazuh rule 100500](screenshots/02-rule-100500.png)

## Configuration

### Falco JSON output
Falco writes JSON events to:
- `/var/log/falco.json`

### Wazuh agent ingestion (ubuntu-docker-host)
Configured `ossec.conf` to ingest Falco JSON:

```xml
<localfile>
  <log_format>json</log_format>
  <location>/var/log/falco.json</location>
</localfile>
