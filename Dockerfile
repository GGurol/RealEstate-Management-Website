# Use the official Python 3.12 slim image as a parent image
FROM python:3.12-slim

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# --- ADDED STEP: Install system dependencies needed for compiling Python packages ---
RUN apt-get update && apt-get install -y \
    # Provides C compilers (gcc) needed for building extensions
    build-essential \
    # Provides development headers for PostgreSQL, required by psycopg[c]
    libpq-dev \
    # Provides development headers for JPEG support, required by Pillow
    libjpeg-dev \
    # Provides development headers for PNG support (compression), required by Pillow
    zlib1g-dev \
    # Clean up apt cache to reduce final image size
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /code

RUN python -m pip install --upgrade pip


# Copy the requirements file and install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy the rest of the project files into the container
COPY . /code/
