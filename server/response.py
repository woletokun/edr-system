# server/response.py
import logging

def handle_response(event: dict, indicators: list):
    """
    Handles detected threats by triggering response actions.

    Currently logs the incident. In a real-world scenario, this could be extended to:
    - Quarantine the host
    - Kill malicious processes
    - Alert security systems (e.g., SIEM)
    - Isolate the endpoint from the network

    Args:
        event (dict): The original event payload from the agent.
        indicators (list): List of detected malicious process names.
    """

    # Extract hostname for logging context
    hostname = event.get("hostname")

    # Log the detected threat and associated indicators
    logging.warning(f"[EDR] Detected threat on {hostname}. Indicators: {indicators}")

    # TODO: Integrate actual response mechanism (e.g., SSH quarantine, kill process)
