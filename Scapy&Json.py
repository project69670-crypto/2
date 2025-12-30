from scapy.all import IP
import json

# נניח שזו חבילה שדגמנו
packet = IP(dst="8.8.8.8", src="192.168.1.1")

# חילוץ נתונים למילון
packet_info = {
    "src": packet.src,
    "dst": packet.dst,
    "proto": packet.proto
}

# המרה ל-JSON (Serialization) כדי שיהיה אפשר לשלוח ב-Socket
json_packet = json.dumps(packet_info)
print(f"Ready to send: {json_packet}")