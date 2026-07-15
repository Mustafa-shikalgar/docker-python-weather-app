# Use the official Python 3.12 slim image as the base image
FROM python:3.12-slim
 
# Set the working directory inside the container
WORKDIR /app
 
# Copy the requirements file to the container
COPY requirements.txt .
 
# Install all required Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
 
# Copy the entire project source code into the container
COPY . .
 
# Run the application when the container starts
CMD ["python", "app.py"]
