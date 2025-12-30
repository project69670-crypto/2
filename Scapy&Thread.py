from scapy.all import sniff
import threading

def start_sniffing():
    print("Sniffer started...")
    # האזנה ל-5 חבילות מידע
    packets = sniff(count=5)
    packets.summary()

# הפעלת ההאזנה ברקע
sniffer_thread = threading.Thread(target=start_sniffing)
sniffer_thread.daemon = True  # מבטיח שה-Thread ייסגר כשהתוכנית הראשית נסגרת
sniffer_thread.start()

print("Main program continues to run while sniffing!")