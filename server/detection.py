# server/detection.py
from typing import Tuple

# Simple rule-based detection: look for suspicious process names
MALICIOUS_PROCESSES = {"malicious.exe", "crypto-miner", "bad_tool"}

def detect_threat(event: dict) -> Tuple[bool, list]:
    suspicious = []
    for proc in event.get("processes", []):
        if proc["name"].lower() in MALICIOUS_PROCESSES:
            suspicious.append(proc["name"])
    return (len(suspicious) > 0, suspicious)
