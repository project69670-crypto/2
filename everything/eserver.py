import socket
import threading
import json

class MultiClientServer:
    def __init__(self, ip, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((ip, port))
        self.sock.listen(5)

    def handle_client(self, conn, addr):
        print(f"Connected to {addr}")
        try:
            # קבלת ה-JSON מהלקוח
            raw_data = conn.recv(1024).decode()
            if raw_data:
                data = json.loads(raw_data) # Deserialization
                print(f"Received from {addr}: {data['packet_summary']}")
        finally:
            conn.close()

    def start(self):
        print("Server is up...")
        while True:
            conn, addr = self.sock.accept()
            # לכל לקוח נפתח Thread נפרד
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()

if __name__ == "__main__":
    MultiClientServer('0.0.0.0', 443).start()