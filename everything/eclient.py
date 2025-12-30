import socket
import json
from scapy.all import sniff


class SniffClient:
    def __init__(self, server_ip, server_port):
        self.server_addr = (server_ip, server_port)

    def get_one_packet(self):
        print("Sniffing one packet...")
        pkt = sniff(count=1)[0]  # דגימת חבילה אחת
        return {"packet_summary": pkt.summary(), "src": pkt.src if 'IP' in pkt else "N/A"}

    def send_data(self):
        # איסוף הנתונים
        packet_info = self.get_one_packet()

        # חיבור ושליחה
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(self.server_addr)
            # המרה ל-JSON ושליחה
            s.send(json.dumps(packet_info).encode())
            print("Data sent!")


if __name__ == "__main__":
    # החליפי ל-IP של השרת שלך
    client = SniffClient('172.20.148.222', 443)
    client.send_data()