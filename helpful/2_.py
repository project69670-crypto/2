from scapy.all import sniff, IP, TCP
import json


def process_packet(packet):
    if IP in packet:
        # יצירת מילון מהנתונים שתפסנו
        packet_info = {
            "src": packet[IP].src,
            "dst": packet[IP].dst,
            "proto": packet[IP].proto
        }

        # המרה ל-JSON (Serialization)
        json_data = json.dumps(packet_info)
        print(f"Captured JSON: {json_data}")

# האזנה ל-5 חבילות בלבד (כדי לא להיתקע בלולאה אינסופית במבחן)
# sniff(count=5, prn=process_packet)