#multi thread
import socket
import threading

def handle_client(client_socket, address):
    print(f"[+] New connection from {address}")
    try:
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            print(f"[*] Received: {data}")
            client_socket.send("OK".encode('utf-8'))
    finally:
        client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 8888))
    server.listen(5)
    print("[*] Server listening on port 8888")

    while True:
        client_sock, addr = server.accept()
        # יצירת תהליכון חדש לכל לקוח כדי שלא יעצרו אחד את השני
        client_handler = threading.Thread(target=handle_client, args=(client_sock, addr))
        client_handler.start()

# start_server()