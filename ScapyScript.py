from scapy.all import *
import time

print("""Custom Packet Sender Script
Created by Joshua Olagunju
========================================================
This script allows you to send ICMP, TCP, or UDP packets 
to a target IP address with a custom payload
====================================================================
⚠️  This script requires root privileges (sudo) to run properly.""")

def user_inputs():
    while True:
        dst_ip = input("Enter the destination IP: ")
        count = int(input("Enter the number of packets to send: "))
        ttl = int(input("Enter the TTL (Time to Live) value: "))
        protocol = input("Enter the Protocol (ICMP, TCP, UDP): ").strip().upper()
        payload = input("Enter the message (payload) to send: ")
        if protocol in ["ICMP", "TCP", "UDP"]:
            return dst_ip, count, ttl, protocol, payload
        else:
            print("Invalid protocol! Choose ICMP, TCP, or UDP.")

def create_packet(dst_ip, count, ttl, protocol, payload):
    if protocol == "TCP":
        transport_layer = TCP(dport=80, flags="S")  
    elif protocol == "UDP":
        transport_layer = UDP(dport=53)
    elif protocol == "ICMP":
        transport_layer = ICMP()
    
    packet = IP(dst=dst_ip, ttl=ttl) / transport_layer / Raw(load=payload)
    
    print("\nPreparing to send packets...")
    time.sleep(3)
    
    for i in range(count):
        response = sr1(packet, timeout=2, verbose=False)
        print(f"Packet {i+1} sent")
        if response:
            print(f"Response received: {response.summary()}")
        else:
            print("No response received.")
    
    print("All packets sent!")
    time.sleep(2)
    print("Thank you for using Scapy")

# **Run the script**
dst_ip, count, ttl, protocol, payload = user_inputs()
create_packet(dst_ip, count, ttl, protocol, payload)
