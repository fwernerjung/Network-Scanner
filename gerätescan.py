import subprocess
import re

def get_connected_devices():
    print("Suche nach Geräten im Netzwerk...")
    devices = []
    
    try:
        # Führt den Windows/Linux-Befehl 'arp -a' aus
        output = subprocess.check_output("arp -a", universal_newlines=True, shell=True)
        
        # Regex, um IP- und MAC-Adressen aus dem Text zu fischen
        # Sucht nach Mustern wie 192.168.x.x
        pattern = re.compile(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+([0-9a-fA-F:-]{17})")
        
        for match in pattern.finditer(output):
            ip, mac = match.groups()
            devices.append({"ip": ip, "mac": mac})
            
    except Exception as e:
        print(f"Fehler beim Auslesen: {e}")
        
    return devices

# Testen
if __name__ == "__main__":
    found_devices = get_connected_devices()
    for d in found_devices:
        print(f"IP: {d['ip']} | MAC: {d['mac']}")