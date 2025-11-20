
# Project 4 – Log Analysis & SIEM (Wazuh)

## 🎯 Objective
Deploy a functional SIEM environment to collect, monitor, and analyze system logs (authentication, file integrity, and process activity) using **Wazuh 4.14 LTS** inside a controlled VirtualBox lab.

---

## 🧩 Lab Setup

| Component | Role | OS / Version | Environment | Notes |
|------------|------|--------------|--------------|--------|
| **Wazuh Server VM** | SIEM Manager + Dashboard + Indexer | Ubuntu 22.04 LTS (OVA v4.14.0) | VirtualBox (Bridged Adapter) | Central log collection & analysis |
| **Kali Linux VM** | Attack / Red-Team Machine | Kali 2025.3 x64 | VirtualBox (Bridged Adapter) | Used to generate attacks |
| **Host OS** | Analyst Workstation | Ubuntu 24.04 | Native | Accesses Wazuh Dashboard via browser |

---

## ⚙️ Quick Start

### 1. Import and Start Wazuh VM
1. Download and import the official Wazuh OVA:  
   [https://documentation.wazuh.com/current/deployment-options/virtual-machine/](https://documentation.wazuh.com/current/deployment-options/virtual-machine/)
2. Assign ≥ 4 vCPUs and 8 GB RAM.  
3. Start the VM and note its IP (e.g., `192.168.1.110`).

### 2. Install Agent on Kali
```bash
curl -sO https://packages.wazuh.com/4.x/apt/pool/main/w/wazuh-agent_4.14.0-1_amd64.deb
sudo dpkg -i wazuh-agent_4.14.0-1_amd64.deb
sudo sed -i 's/<address>.*<\/address>/<address>192.168.1.110<\/address>/' /var/ossec/etc/ossec.conf
sudo systemctl enable --now wazuh-agent
