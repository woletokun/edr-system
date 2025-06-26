# server/main.py

from flask import Flask, request, jsonify
from server.models import verify_signature
from server.detection import detect_threat
from server.response import handle_response

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "✅ EDR Server is running. POST events to /api/events", 200


@app.route("/api/events", methods=["POST"])
def receive_event():
    payload = request.json
    if not verify_signature(payload):
        return jsonify({"error": "Invalid signature"}), 401

    threats = detect_threat(payload)
    if threats:
        handle_response(payload, threats)
        return jsonify({"status": "threats_detected", "threats": threats}), 200

    return jsonify({"status": "clean"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
