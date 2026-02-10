# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies for Selenium
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    wget \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements first (Docker cache best practice)
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy rest of the project
COPY . /app

# Environment variables for Chrome
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

# Run Behave
CMD ["behave", "Features"]
