# server/api.py
from flask import Flask, request, jsonify
from detection import detect_threat
from response import handle_response
from models import validate_event, verify_signature
import os

app = Flask(__name__)
SECRET_KEY = os.getenv("SECRET_KEY", "devkey")

@app.route("/api/events", methods=["POST"])
def receive_event():
    payload = request.get_json(force=True)
    sig = request.headers.get("X-Signature", "")

    # Validate signature and payload structure
    if not verify_signature(payload, sig, SECRET_KEY):
        return jsonify({"error": "Invalid signature"}), 401
    if not validate_event(payload):
        return jsonify({"error": "Invalid payload"}), 400

    # Detection logic
    is_threat, indicators = detect_threat(payload)

    # Response action
    if is_threat:
        handle_response(payload, indicators)

    return jsonify({"received": True, "threat_detected": is_threat}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
