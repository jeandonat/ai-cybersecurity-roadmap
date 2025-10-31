# Project 5 – Mini SOC Simulation

---

## 🎯 Objective
Combine your scanner, monitoring, and SIEM tools into a cohesive **local Security Operations Center (SOC)**.  
Simulate attacks (e.g. nmap scans, brute-force attempts) and build **automated response scripts** to detect, alert, and react.

Duration ≈ 20 hours

---

## 🧩 Scope & Deliverables
| Component | Description | Tools / Tech |
|------------|--------------|---------------|
| **Attack Simulation** | Generate network noise (port scans, brute-force, etc.) | `nmap`, `hydra`, `hping3` |
| **Detection** | Capture and analyze alerts in your SIEM | Wazuh / Splunk |
| **Response Automation** | Block malicious IPs or trigger notifications | Bash / Python / UFW |
| **Documentation** | Architecture, screenshots, runbook | Markdown + Images |

Deliverables:
- Local Mini-SOC architecture diagram  
- Working attack simulation script  
- Auto-response mechanism  
- Dashboard screenshots showing alerts  
- Complete runbook for incident workflow

---

## ⚙️ Setup Instructions

1. **Ensure Projects 1–4 are complete:**
   - Hardened Linux environment (UFW, Fail2Ban, no root SSH)
   - Active network monitoring (`tcpdump`, `Wireshark`)
   - Vulnerability scanner (OpenVAS or Nessus)
   - Configured SIEM (Wazuh or Splunk)

2. **Clone or pull latest repo:**
   ```bash
   git pull origin main
