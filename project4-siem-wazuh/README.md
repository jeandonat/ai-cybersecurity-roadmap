# Project 4 — Log Analysis & SIEM (Wazuh)

Goal: collect & analyze security logs (auth, FIM, process) with Wazuh.

## Quick Start
- Bring up Wazuh:
  mkdir -p ~/wazuh && cd ~/wazuh
  curl -sLO https://packages.wazuh.com/4.7/docker-compose.yml
  docker compose -f docker-compose.yml -p wazuh up -d  # UI: https://127.0.0.1:5601

- Install agent (Ubuntu host):
  curl -s https://packages.wazuh.com/key/GPG-KEY-WAZUH | sudo apt-key add -
  echo "deb https://packages.wazuh.com/4.x/apt/ stable main" | sudo tee /etc/apt/sources.list.d/wazuh.list
  sudo apt update && sudo apt install -y wazuh-agent
  sudo sed -i 's#<address>.*</address>#<address>127.0.0.1</address>#' /var/ossec/etc/ossec.conf
  sudo systemctl enable --now wazuh-agent

## Generate Sample Events
# failed SSH attempts
for i in {1..5}; do sudo ssh -o StrictHostKeyChecking=no -l wronguser localhost 'exit' || true; done
# FIM (file change)
sudo tee -a /var/ossec/etc/ossec.conf >/dev/null <<'X'
<syscheck><directories check_all="yes">/etc</directories></syscheck>
X
sudo systemctl restart wazuh-agent
sudo sh -c 'echo test > /etc/wazuh-fim-demo.txt'; sudo rm /etc/wazuh-fim-demo.txt

## Artifacts to save (./artifacts/)
- Security Events (failed logins) screenshot
- Integrity Monitoring alert screenshot
- Agent status screenshot
