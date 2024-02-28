# Use a base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the Hangman game files
COPY hangman.py .
COPY words.txt .

# Expose SSH port
EXPOSE 22

# Command to start SSH server
CMD ["python", "hangman.py"]
