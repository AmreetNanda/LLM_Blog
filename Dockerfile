# -------- Base Image --------
# Use official Python slim image
FROM python:3.11-slim

# -------- Environment Setup --------
# Avoid buffering outputs
ENV PYTHONUNBUFFERED=1
# Prevent Streamlit from opening a browser inside container
ENV STREAMLIT_SERVER_HEADLESS=true
# Allow Streamlit to run on all network interfaces
ENV STREAMLIT_SERVER_PORT=8501

# -------- System dependencies --------
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# -------- Set working directory --------
WORKDIR /app

# -------- Copy project files --------
COPY . /app

# -------- Install Python dependencies --------
RUN pip install --upgrade pip
RUN pip install --no-cache-dir \
    streamlit \
    langchain \
    langchain_community \
    ctransformers

# Optional: If you have requirements.txt, use:
# COPY requirements.txt /app/
# RUN pip install --no-cache-dir -r requirements.txt

# -------- Expose port --------
EXPOSE 8501

# -------- Entry point --------
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
