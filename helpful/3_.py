import json

# מילון פייתון (Object)
my_data = {"status": "success", "users": ["Alice", "Bob"], "id": 101}

# 1. הפיכה למחרוזת JSON כדי לשלוח ב-Socket
json_string = json.dumps(my_data)
# שליחה: client_socket.send(json_string.encode())

# 2. קבלה מה-Socket והפיכה חזרה למילון
# received_data = client_socket.recv(1024).decode()
data_dict = json.loads(json_string)

print(data_dict["users"][0]) # ידפיס: Alice