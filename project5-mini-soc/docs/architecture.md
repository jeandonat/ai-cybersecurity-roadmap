# Mini SOC Architecture

## Components
- Wazuh Manager (Ubuntu 24.04)
- Wazuh Indexer + Dashboard (Docker single-node)
- Wazuh Agent (Kali Linux)

## Data Flow
1. Logs from Kali → Agent → Manager → Indexer → Dashboard

## Use Case
- Detect SSH brute-force attempts
- Detect system file tampering
