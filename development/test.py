import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tools.gerätescan import get_connected_devices

found_devices = get_connected_devices()

for d in found_devices:
    print(f"IP: {d['ip']} | MAC: {d['mac']}")