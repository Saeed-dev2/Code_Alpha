# Network Sniffer in Python

## Project Overview
This project is a **Network Sniffer** built using Python and the `scapy` library. The sniffer captures and analyzes network packets in real-time, providing detailed information about the source and destination IPs, protocols, and port numbers for TCP and UDP packets. This tool is ideal for understanding how data flows on a network and learning about network packet structure.

---

## Features
- **Packet Capturing**: Captures all IP packets on the network.
- **Protocol Analysis**: Identifies the protocol (TCP or UDP) used by the packet.
- **Source and Destination Details**: Displays source IP, destination IP, source port, and destination port.
- **Real-Time Output**: Provides immediate insights into network activity as packets are captured.

---

## Prerequisites
Before running the script, ensure you have the following installed and configured:
- **Python 3.x**: Required for running the script.
- **Scapy Library**: Install using:
  ```bash
  pip install scapy


## Setup Instructions

### Clone the Repository
```bash
git clone https://github.com/your-username/cloud-based-photo-gallery.git
cd cloud-based-photo-gallery
```

## Install Dependencies
```bash
pip install scapy
```
## Run the Script



```bash
sudo python network_sniffer.py
```
## Output

Source IP: 192.168.1.100 -> Destination IP: 8.8.8.8 | Protocol: 6
TCP Packet | Source Port: 43567 -> Destination Port: 80
--------------------------------------------------
