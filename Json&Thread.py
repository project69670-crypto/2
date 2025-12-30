import threading
import json

def process_data(json_string):
    # הפיכת מחרוזת JSON למילון פייתון (Deserialization)
    data = json.loads(json_string)
    print(f"Thread {threading.current_thread().name} processing: {data['user']}")

# נתונים לדוגמה
message = '{"user": "Student", "command": "SCAN"}'

# יצירת Thread והעברת ה-JSON כארגומנט
t = threading.Thread(target=process_data, args=(message,))
t.start()