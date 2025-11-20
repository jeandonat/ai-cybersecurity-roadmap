
# Project 5 – Mini SOC Simulation

## 🎯 Objective
Build a **local Security Operations Center (SOC)** using your existing tools — combining scanning, monitoring, and SIEM analytics to detect, correlate, and respond to simulated cyber-attacks in real time.

This stage transitions your lab from passive log collection (Project 4) to **active defense and threat response**.

---

## 🧩 Environment Overview

| Component | Role | OS / Version | Environment | Notes |
|------------|------|--------------|--------------|--------|
| **Wazuh VM** | SIEM Manager + Dashboard + Indexer | Ubuntu 22.04 LTS (OVA v4.14) | VirtualBox – Bridged Adapter | Central log correlation and alerting |
| **Kali VM** | Attacker / Red-Team | Kali 2025.3 x64 | VirtualBox – Bridged Adapter | Generates scans and attacks |
| **Host Machine** | Analyst / SOC Operator | Ubuntu 24.04 LTS | Native | Access to dashboard and scripts |

---

## ⚙️ Prerequisites
Make sure you’ve completed:
- **Project 1 – Linux Hardening**
- **Project 2 – Network Monitoring**
- **Project 3 – Vulnerability Scanning**
- **Project 4 – Log Analysis & SIEM**

The **Wazuh VM** should already have the **Kali agent** connected and reporting successfully.

---

## 🚀 Step 1 – Attack Simulations (from Kali)

### 🔍 1. Network Reconnaissance
Simulate a port scan against the Wazuh server.
```bash
sudo nmap -sS -T4 192.168.1.110
