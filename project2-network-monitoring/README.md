Project 2 – Network Monitoring

Part of my AI-Driven Cybersecurity Roadmap

Goal

Monitor network activity on a hardened Linux workstation by capturing, filtering, and analyzing live traffic.

Objective

Capture baseline network traffic to identify normal patterns, understand the use of DNS, TCP, and UDP, and document results for comparison in future monitoring projects.

Tools Used

tcpdump

Wireshark

Bash

Steps

Installed tcpdump and Wireshark.

Captured 200 packets using sudo tcpdump -i any -c 200 -w baseline_traffic.pcap.

Viewed a summary in the terminal with tcpdump -r baseline_traffic.pcap -n | head -20.

Opened the capture in Wireshark and filtered by protocol (dns, tcp, udp, tcp.port == 443).

Reviewed DNS lookups, TCP handshakes, and QUIC (UDP 443) traffic.

Documented findings in analysis logs and screenshots.

Results

DNS resolution observed for web.whatsapp.com (UDP 53).
Project 2 – Network Monitoring

Part of my AI-Driven Cybersecurity Roadmap

Goal

Establish basic network visibility on a hardened Linux workstation by capturing, filtering, and analyzing live traffic.

Objective

Observe normal outbound and local traffic, identify key protocols (DNS, TCP, UDP), and document baseline behavior to serve as a reference for future anomaly detection.

Tools Used

tcpdump

Wireshark

Bash

Steps

Installed tcpdump and Wireshark.

Captured a short sample of live traffic with
sudo tcpdump -i any -c 200 -w baseline_traffic.pcap.

Reviewed packets in the terminal using
tcpdump -r baseline_traffic.pcap -n | head -20.

Opened the capture in Wireshark for detailed analysis.

Applied filters such as dns, tcp, udp, and tcp.port == 443 to isolate protocols.

Documented observations and saved analysis results in text logs.

Results

DNS requests successfully captured and resolved (web.whatsapp.com → 157.240.17.60).

Normal HTTPS and QUIC traffic observed on port 443.

No abnormal or unauthorized connections detected.

Verified visibility across TCP, UDP, and ICMP traffic.

Evidence

logs/baseline_traffic.pcap – raw packet capture

logs/baseline_analysis.txt – tcpdump summary

logs/wireshark_analysis.txt – Wireshark findings

screenshots/screenshot_tcpdump_baseline.png – terminal output

Lessons Learned

DNS operates over UDP 53 and maps human-readable domains to IP addresses.

TCP provides reliable, connection-based transport for HTTPS traffic.

UDP enables fast, connectionless protocols such as QUIC.

tcpdump is ideal for quick command-line captures; Wireshark provides deep inspection and filtering.

Summary

Network monitoring confirms the hardened system communicates normally with external services using secure protocols.
Baseline logs and packet captures are stored in the repository for future comparison during threat-detection exercises.
HTTPS and QUIC connections identified on port 443.

Normal encrypted communication between local host and remote servers.

No unusual or unauthorized connections detected.

Evidence

baseline_traffic.pcap – captured packets

baseline_analysis.txt – tcpdump summary

wireshark_analysis.txt – Wireshark review

Screenshots in /screenshots

Proof	Description
baseline_traffic.pcap	Raw network capture file
wireshark_analysis.txt	Filtered analysis results
screenshot_tcpdump_baseline.png	Packet capture summary
Lessons Learned

Monitoring live traffic helps visualize how DNS queries and encrypted connections operate.
tcpdump provides fast terminal-based visibility, while Wireshark offers detailed inspection and filtering for network analysis.

Summary

Normal DNS, TCP, UDP, and QUIC activity was recorded and analyzed.
The capture established a baseline of legitimate network behavior, which will be used as reference data for future anomaly and threat detection exercises.
