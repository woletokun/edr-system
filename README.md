# 🛡️ Endpoint Detection and Response (EDR) System

A lightweight, modular Endpoint Detection and Response (EDR) system built in Python for monitoring, detecting, and responding to malicious activities on endpoint devices.

---

## 📌 Features

- 📥 **Agent-Based Monitoring**: Collects process activity, user info, and system events from endpoints  
- 🧠 **Rule-Based Threat Detection**: Detects known malicious processes with customizable logic  
- 🔐 **Secure Communication**: Uses HMAC signatures to verify and trust event data from endpoints  
- 🚨 **Automated Response**: Logs alerts and allows for pluggable remediation (e.g., quarantine, notification)  
- 🧪 **Unit & Integration Tests**: Coverage for detection logic, agent payloads, and response triggers  
- 🐳 **Dockerized**: Containerized services with `docker-compose` support for development and deployment

---

## 🏗️ Architecture

┌────────┐ REST API ┌────────────┐ Detection ┌────────────┐
│ Agent ├──────────────────────►│ Server ├──────────────────────►│ Engine │
└────────┘ └────────────┘ └────────────┘
▲ │
│ Response Triggering ▼
└──────────────────────────────────────────────────────────────────┐
▼
┌────────────────────┐
│ Response API │
└────────────────────┘

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.8+
- Git
- Docker & Docker Compose *(optional, for containerized setup)*
- `gh` CLI *(optional, for managing GitHub repo)*

---

### 📦 Installation (Local Dev)

```bash
# Clone the repo
git clone https://github.com/tokstokun/edr-system.git
cd edr-system

# Set up a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
pytest tests/

# Run with Docker
docker-compose up --build

edr-system/
├── agent/                  # Lightweight Python agent
├── server/                 # Flask API server with detection/response logic
├── tests/                  # Unit and integration tests
├── docker-compose.yml      # Docker environment
├── requirements.txt
└── README.md

**Detection Logic**
The detection engine currently uses a static rule list:
MALICIOUS_PROCESSES = {"malicious.exe", "crypto-miner"}

This can be expanded into:
YARA rule integration
Machine learning models
Behavioral profiling

**Security Considerations**
All data is HMAC-signed using a shared secret key
Input is validated against expected schema before processing
Supports future mTLS encryption for agent-server traffic

**Author
Oyewole Olatokun**


