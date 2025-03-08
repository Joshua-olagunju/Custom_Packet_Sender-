# Custom_Packet_Sender-

## Overview  
This script, created by **Joshua Olagunju**, allows users to send ICMP, TCP, or UDP packets to a target IP address with a custom payload.  

⚠ **Note:** This script requires root privileges (sudo) to run properly.  

## Features  
- Sends **ICMP, TCP, or UDP** packets  
- Allows users to specify **destination IP, packet count, TTL, and payload**  
- Displays response summary if received  
- Works on **Kali Linux** and other Linux distributions with **Scapy installed**  

## Installation  
Ensure you have **Scapy** installed:  
```
sudo apt update && sudo apt install python3-scapy
```
## Usage
Run the script with sudo:
```
sudo python3 ScapyScript.py
```
Then enter the required details when prompted.

## Example Output
```
Enter the destination IP: 10.6.6.23  
Enter the number of packets to send: 5  
Enter the TTL (Time to Live) value: 15  
Enter the Protocol (ICMP, TCP, UDP): TCP  
Enter the message (payload) to send: i love python  

Preparing to send packets...
Packet 1 sent  
Response received: IP / TCP 10.6.6.23:http > 10.6.6.1:ftp_data SA  
...
All packets sent!  
Thank you for using Scapy
```
## Issues & Feedback
If you encounter any issues or have suggestions for improvement, feel free to comment or open an issue in this repository.

## License
This project is licensed under the MIT License.
