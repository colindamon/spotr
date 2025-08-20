FROM python:3.13.6-slim

# Set work directory in container
WORKDIR /app

# Install system dependencies (if needed for torch/torchvision; comment out if not needed)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend, frontend, and models folders
COPY backend/ backend/
COPY frontend/ frontend/
COPY models/ models/

# Expose ports for backend and frontend
EXPOSE 8000 8501