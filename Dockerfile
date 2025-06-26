FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files (not just subfolders)
COPY . .

# Set Python path so 'server' can be imported
ENV PYTHONPATH=/app

# Expose the Flask port
EXPOSE 5000

# Run the Flask app
CMD ["python", "server/main.py"]
