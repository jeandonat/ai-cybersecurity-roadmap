# Incident Report — Interactive Shell in Container

## Summary
An interactive shell was detected inside a DVWA Docker container on host `jedi-pc`.  
The behavior was identified by Falco using syscall-level runtime analysis and correlated in Wazuh for investigation and timeline reconstruction.

## Detection
- Tool: Falco
- Rule: Terminal shell in container
- Timestamp: 2026-02-02 15:08:17
- Container: dvwa
- Image: vulnerables/web-dvwa:latest
- User: root
- MITRE ATT&CK: T1059 – Command and Scripting Interpreter

## Investigation
The Falco alert was ingested into Wazuh and correlated with host-level context on the Docker host.  
Manual pivoting by timestamp and host confirmed the activity occurred within the same time window and environment.

## Impact Assessment
Spawning an interactive shell inside a web application container is not expected behavior and may indicate:
- post-exploitation access
- webshell escalation
- unauthorized administrative interaction
- misconfigured container security controls

## Remediation Recommendations
- Restrict interactive shell access to containers
- Apply least-privilege container configurations
- Monitor runtime behavior using syscall-based detection
- Integrate runtime alerts into centralized SOC workflows

## Status
Contained (lab environment).

