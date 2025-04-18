# Use an official Python runtime as a parent image
FROM python:3.11-slim-bookworm

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the content of the current directory to the working directory
COPY . .

# Make port 80 available to the outside world
EXPOSE 8000

# Define environment variable
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8000

# Run app.py when the container launches
#CMD ["flask", "run"]

# Use gunicorn as the WSGI server
CMD ["gunicorn", "main:app", "-w", "4", "-b", "0.0.0.0:8000"]