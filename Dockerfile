# Use a slim Python 3.11 image to keep the container small
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies needed for PDF processing (PyMuPDF)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install uv (our fast package manager)
RUN pip install uv

# Copy project files needed for installation
COPY pyproject.toml .
COPY uv.lock .

# Install dependencies
RUN uv pip install --system .

# Copy the rest of your application code
COPY . .

# Pre-download the BERT model to the container during build 
# This prevents the app from downloading it every time it starts
RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2')"

# Expose the port for Streamlit
EXPOSE 8501

# Command to run your app
CMD ["streamlit", "run", "src/app.py", "--server.port=8501", "--server.address=0.0.0.0"]