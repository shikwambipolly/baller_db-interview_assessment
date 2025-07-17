FROM python:3.8-slim

# Install system dependencies including netcat
#RUN apt-get update && apt-get install -y netcat && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy and set entrypoint
COPY start.sh /start.sh
RUN chmod +x /start.sh
ENTRYPOINT ["/start.sh"]

# Expose port
EXPOSE 8000

# Default command
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
