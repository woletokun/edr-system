# agent/agent.py
import os, socket, requests
import psutil
from utils import load_config, sign_payload

CONFIG = load_config()

def collect_data():
    """
    Collect basic endpoint telemetry: hostname and running processes.
    Expandable with file monitoring, network activity, etc.
    """
    return {
        "hostname": socket.gethostname(),
        "user": os.getlogin(),
        "processes": [
            {"pid": p.pid, "name": p.name(), "exe": p.exe()}
            for p in psutil.process_iter(attrs=['pid','name','exe'])
        ],
    }

def send_data(data):
    """
    Send event data to central server with HMAC signature for trust.
    """
    headers = {
        "Content-Type": "application/json",
        "X-Signature": sign_payload(data, CONFIG["secret_key"])
    }
    resp = requests.post(CONFIG["server_url"] + "/api/events", json=data, headers=headers, timeout=5)
    resp.raise_for_status()
    return resp.json()

if __name__ == "__main__":
    data = collect_data()
    print("[Agent] Sending data:", data)
    result = send_data(data)
    print("[Agent] Server response:", result)

