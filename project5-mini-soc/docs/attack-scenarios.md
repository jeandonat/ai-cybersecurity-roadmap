# Attack Scenarios

## SSH Bruteforce
for i in {1..5}; do ssh -l wronguser localhost 'exit' || true; done

## FIM Trigger
sudo nano /etc/hosts
