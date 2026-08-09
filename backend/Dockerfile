
# Start with a Python base image
FROM python:3.11-slim

# Create a working directory inside the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files into the container
COPY . .

# Document the port used by Flask
EXPOSE 7860

# Start the Flask application
CMD ["python", "app.py"]
