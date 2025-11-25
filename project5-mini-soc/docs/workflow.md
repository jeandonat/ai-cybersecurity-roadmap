# Detection & Response Workflow

1. Attacker performs failed SSH logins on Kali.
2. Wazuh Agent sends logs to Manager.
3. Manager triggers rule 5710/5712.
4. Analyst reviews and responds (block IP, check persistence).
