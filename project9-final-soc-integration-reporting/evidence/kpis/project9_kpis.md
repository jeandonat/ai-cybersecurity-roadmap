## SOC KPIs — Project 9

| KPI | Value | Notes |
|----|------|------|
| Detection Source | Falco (runtime) | Syscall-based container monitoring |
| Mean Time to Detect (MTTD) | < 1 second | Runtime execution detected immediately |
| Mean Time to Investigate (MTTI) | ~2 minutes | Manual correlation via Wazuh timeline |
| Alert Confidence | High | Interactive shell in web container |
| False Positives | Low | DVWA container should not spawn shells |
| MITRE ATT&CK Coverage | T1059 | Command & Scripting Interpreter |

