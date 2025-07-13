FROM python:3.12-slim

WORKDIR /app

# Install build tools (optional but often needed for some packages like bcrypt)
RUN apt-get update && apt-get install -y \
    build-essential gcc && \
    rm -rf /var/lib/apt/lists/*

# Copy pyproject.toml and install dependencies
COPY pyproject.toml .
RUN pip install --upgrade pip && pip install --no-cache-dir .

# Copy the app source code
COPY . .

# Expose port and run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

