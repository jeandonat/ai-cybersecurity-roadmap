# Wazuh Agent Setup on Kali

Commands:
sudo apt install wazuh-agent
sudo systemctl enable --now wazuh-agent

Verification:
systemctl status wazuh-agent
tail -f /var/ossec/logs/ossec.log
