
from scapy.all import sniff, TCP, UDP, IP

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto

        print(f"Source IP: {ip_src} -> Destination IP: {ip_dst} | Protocol: {protocol}")

        if packet.haslayer(TCP):
            print(f"TCP Packet | Source Port: {packet[TCP].sport} -> Destination Port: {packet[TCP].dport}")
        elif packet.haslayer(UDP):
            print(f"UDP Packet | Source Port: {packet[UDP].sport} -> Destination Port: {packet[UDP].dport}")
        print("-" * 50)

print("Starting the network sniffer... Press Ctrl+C to stop.")
sniff(filter="ip", prn=packet_callback, store=0)
