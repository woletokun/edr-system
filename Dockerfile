# Dockerfile

FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY server/ ./server
COPY agent/ ./agent

# Expose the port Flask will run on
EXPOSE 5000

# Default command to run the Flask app
CMD ["python", "server/main.py"]
