# --- Stage 1: Build Stage ---
# Use a slim image to install dependencies
FROM python:3.11-slim AS builder

WORKDIR /app

# Install dependencies into a virtual environment to keep things clean
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy and install requirements (assuming you have a requirements.txt)
# For just Flask, you can run: RUN pip install flask
RUN pip install --no-cache-dir flask

# --- Stage 2: Final Run Stage ---
# Use the same slim image for the final, clean layer
FROM python:3.11-slim

WORKDIR /app

# Copy the virtual environment from the builder stage
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy your application code
COPY app.py .

# Expose the port your app runs on
EXPOSE 3000

# Run the application
CMD ["python", "app.py"]
