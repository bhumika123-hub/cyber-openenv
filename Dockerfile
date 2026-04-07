# Use stable slim image
FROM python:3.10-slim

# Prevent python buffering
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy requirements first (better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Expose port (important for API)
EXPOSE 7860

# Start your app
CMD ["python", "server/app.py"]
