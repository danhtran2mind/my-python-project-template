# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements.txt to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY flask_app.py .
COPY fastapi_app.py .
COPY streamlit_app.py .
COPY gradio_app.py .

# Expose ports for Flask (5000), FastAPI (8000), Streamlit (8501), and Gradio (7860)
EXPOSE 5000 8000 8501 7860

# Command to run the app (default to Flask; override in docker-compose or run command)
CMD ["python", "flask_app.py"]
