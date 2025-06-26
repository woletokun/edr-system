# server/detection.py
from typing import Tuple

# Set of known malicious process names (can be extended with external signatures or models)
MALICIOUS_PROCESSES = {"malicious.exe", "crypto-miner", "bad_tool"}

def detect_threat(event: dict) -> Tuple[bool, list]:
    """
    Detects whether any known malicious processes are present in the given event.

    Args:
        event (dict): The incoming event data containing a list of running processes.

    Returns:
        Tuple[bool, list]: 
            - A boolean indicating if threats were detected.
            - A list of the detected malicious process names.
    """
    suspicious = []

    # Loop through all processes sent in the event payload
    for proc in event.get("processes", []):
        # Normalize process name and check against known malicious ones
        if proc["name"].lower() in MALICIOUS_PROCESSES:
            suspicious.append(proc["name"])

    # Return whether any threats were found, along with the list
    return (len(suspicious) > 0, suspicious)

