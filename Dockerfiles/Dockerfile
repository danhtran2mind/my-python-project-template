#!/bin/bash

# Create Dockerfiles directory if it doesn't exist
mkdir -p Dockerfiles

# Create Dockerfile
cat << EOF > Dockerfiles/Dockerfile
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
EOF

# Create requirements.txt
cat << EOF > requirements.txt
flask==2.3.3
fastapi==0.115.0
uvicorn==0.30.6
streamlit==1.39.0
gradio==4.44.0
EOF

# Build the Docker image
echo "Building Docker image..."
docker build -t my-python-apps -f Dockerfiles/Dockerfile .

# Add files to Git (assuming Git is already initialized)
git add Dockerfiles/Dockerfile requirements.txt
git commit -m "Add Dockerfile and requirements.txt for containerizing Python apps"
git push origin main

# Optional: Run the container for one of the apps (uncomment the desired command)
# echo "Running Flask app..."
# docker run -p 5000:5000 my-python-apps

# echo "Running FastAPI app..."
# docker run -p 8000:8000 my-python-apps uvicorn fastapi_app:app --host 0.0.0.0 --port 8000

# echo "Running Streamlit app..."
# docker run -p 8501:8501 my-python-apps streamlit run streamlit_app.py --server.port 8501 --server.address 0.0.0.0

# echo "Running Gradio app..."
# docker run -p 7860:7860 my-python-apps python gradio_app.py