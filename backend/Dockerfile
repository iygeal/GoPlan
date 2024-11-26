# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set the working directory to backend/
WORKDIR /backend

# Install system dependencies required for mysqlclient
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    default-libmysqlclient-dev \
    pkg-config \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy only the requirements.txt first for dependency installation
COPY requirements.txt /backend/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire backend folder into the container
COPY . /backend/

# Expose the port the app runs on
EXPOSE 5000

# Set environment variables (optional for debugging)
ENV FLASK_ENV=development

# Run the application
CMD ["python", "run.py"]
