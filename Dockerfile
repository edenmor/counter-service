# Use an official Python runtime as a parent image
FROM python:3.8-slim
# Set the working directory in the container
WORKDIR /app
# Copy the dependencies file to the working directory
COPY requirements.txt .
# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 80
ENV FLASK_APP=payoneer.py
# Run the application when the container launches
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]

