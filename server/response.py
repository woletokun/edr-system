# server/response.py
import logging

def handle_response(event: dict, indicators: list):
    """
    Invoke remedial actions, e.g., alerting, isolating host.
    Currently logs and simulates quarantine.
    """

    hostname = event.get("hostname")
    logging.warning(f"[EDR] Detected threat on {hostname}. Indicators: {indicators}")
    # TODO: Integrate with orchestration (SSH, agent command, network quarantine)
