"""
server/main.py
--------
Flask-based API server for receiving signed endpoint events from agents,
verifying authenticity, detecting threats, and triggering responses.
"""

from flask import Flask, request, jsonify
from server.models import verify_signature
from server.detection import detect_threat
from server.response import handle_response

# Initialize the Flask app
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    """
    Root route for health check.
    Returns a simple message to indicate the server is running.
    """
    return "✅ EDR Server is running. POST events to /api/events", 200

@app.route("/api/events", methods=["POST"])
def receive_event():
    """
    Main endpoint for agent event submission.
    Expects a JSON payload containing endpoint telemetry and a valid HMAC signature.
    """
    payload = request.json

    # Security: Verify the payload's HMAC signature
    if not verify_signature(payload):
        return jsonify({"error": "Invalid signature"}), 401

    # Analyze the payload for potential threats
    threats = detect_threat(payload)

    # If threats are found, trigger the response engine
    if threats:
        handle_response(payload, threats)
        return jsonify({"status": "threats_detected", "threats": threats}), 200

    # No threats found
    return jsonify({"status": "clean"}), 200

if __name__ == "__main__":
    # Start the Flask server on all interfaces at port 5000
    app.run(host="0.0.0.0", port=5000)
