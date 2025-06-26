# agent/agent.py
import os, socket, requests
import psutil
from utils import load_config, sign_payload

# Load agent configuration (e.g., server URL, secret key)
CONFIG = load_config()

def collect_data():
    """
    Collects basic telemetry from the host.

    Gathers:
        - Hostname
        - Current logged-in user
        - List of running processes (PID, name, and executable path)

    Returns:
        dict: Structured event payload
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
    Sends collected data to the EDR server with an HMAC signature.

    Args:
        data (dict): The telemetry payload to send.

    Returns:
        dict: JSON response from the server.

    Raises:
        HTTPError: If the server returns an error status.
    """
    headers = {
        "Content-Type": "application/json",
        "X-Signature": sign_payload(data, CONFIG["secret_key"])
    }

    # Send POST request to the EDR server's /api/events endpoint
    resp = requests.post(CONFIG["server_url"] + "/api/events", json=data, headers=headers, timeout=5)

    # Raise exception on non-2xx responses (useful for logging or retry logic)
    resp.raise_for_status()
    return resp.json()

if __name__ == "__main__":
    # Collect and send telemetry when the script is run directly
    data = collect_data()
    print("[Agent] Sending data:", data)
    result = send_data(data)
    print("[Agent] Server response:", result)
