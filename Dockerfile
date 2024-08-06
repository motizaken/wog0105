# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Copy the dummy_scores.txt file into the container
COPY ./app/dummy_scores.txt /app/scores.txt

# Expose the port the app runs on
EXPOSE 5001

# Define the command to run the application
CMD ["python", "main_score.py"]
