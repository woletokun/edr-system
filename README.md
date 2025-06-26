# 🛡️ Endpoint Detection and Response (EDR) System

A lightweight, modular EDR system built in Python to monitor, detect, and respond to malicious activities on endpoint devices. This project demonstrates secure agent-server communication, rule-based threat detection, and real-world DevSecOps practices — including automated testing and Dockerized deployment.

---

## 📢 Project Summary for Reviewers

This system was developed as a practical security-focused DevOps demonstration, featuring:

* 🔗 Agent-server event flow with HMAC-signed payloads
* 🧠 Static rule-based detection engine (extendable to ML/YARA)
* ✅ Unit/integration testing with CI/CD compatibility
* 🐳 Dockerized architecture for portability and scalability
* 🔧 Designed for future enhancements like process isolation, mTLS, or behavioral analysis

---

## 📌 Features

* 📥 **Agent-Based Monitoring**
  Simulates endpoint activity by sending process/user data to the server

* 🧠 **Rule-Based Threat Detection**
  Detects known threats using a customizable detection engine

* 🔐 **Secure Communication**
  All events are HMAC-signed to prevent tampering or spoofing

* 🚨 **Automated Response Handling**
  Logs threats and supports future extensions (e.g., kill process, quarantine)

* 🧪 **Unit & Integration Tests**
  Pytest test suite covering signature verification, detection logic, and response flow

* 🐳 **Dockerized Deployment**
  One-line setup using `docker-compose` for seamless local or CI/CD deployment

---

## 🏧 System Architecture

```
🔌 Agent ➔ Server (Flask) ➔ Detection Logic ➔ Response Handler
     │                  ↑
     │                  └── HMAC-Signed POST /api/events
                             │
                             ↓
                         Alert / Log
```

---

## 🚀 Getting Started

### 🔧 Prerequisites

* Python 3.8+
* Git
* Docker & Docker Compose *(optional but recommended)*
* GitHub CLI `gh` *(optional)*

---

### 🛠️ Installation (Local Development)

```bash
# Clone the repo
git clone https://github.com/tokstokun/edr-system.git
cd edr-system

# (Optional) Virtual environment
python -m venv venv

# Activate:
# Linux/macOS:
source venv/bin/activate
# Windows:
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/

# Run with Docker
docker-compose up --build
```

---

## 📁 Project Structure

```
edr-system/
├── agent/                  # Simulated endpoint agent
├── server/                 # Flask API with detection/response logic
│   ├── main.py             # API entry point
│   ├── models.py           # Signature verification
│   ├── detection.py        # Threat detection logic
│   └── response.py         # Response handler
├── tests/                  # Pytest test suite
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## ⚙️ Detection Logic

The detection engine uses a static rule list:

```python
MALICIOUS_PROCESSES = {"malicious.exe", "crypto-miner"}
```

It can be expanded to:

* 🔍 YARA rule matching
* 🤖 ML-based anomaly detection
* 📊 Behavioral profiling or baseline deviations

---

## 🔐 Security Considerations

* ✅ All data is HMAC-signed with a shared secret
* ✅ Payloads are validated before processing
* ✅ Designed for mTLS, token auth, or API key integration

---

## 🧪 Testing & CI

* Tests written with `pytest`
* Covers:

  * Agent payloads
  * Signature validation
  * Threat detection
  * Response handler
* GitHub Actions CI with `PYTHONPATH=.` configured

