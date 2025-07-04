import os
import sys

import requests
import psutil

def get_app_path():
    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle (PyInstaller)
        return os.path.dirname(sys.executable)
    else:
        # If the application is run as a script
        return os.path.dirname(os.path.abspath(__file__))

app_path = get_app_path()
snitch_path = os.path.join(app_path, "snitch.txt")

with open(snitch_path, "r") as f:
    SNITCH_URL = f.read().strip()

def is_plex_running():
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == "Plex Media Server.exe":
            return True
    return False

def ping_snitch():
    try:
        r = requests.get(SNITCH_URL, timeout=10)
        print(f"Pinged snitch, status: {r.status_code}")
        # print("Plex is running, pinging snitch...")
    except Exception as e:
        print(f"Could not ping snitch: {e}")

if __name__ == "__main__":
    if is_plex_running():
        ping_snitch()
    else:
        print("Plex is not running; not pinging snitch.")
