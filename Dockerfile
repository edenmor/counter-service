# Use an official Python runtime as a parent image
FROM python:3.8-alpine
# Set the working directory in the container
WORKDIR /app
# Copy the dependencies file to the working directory
COPY requirements.txt .
# Install  dependencies
RUN apk update && apk add curl 
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8080
ENV REDIS_HOST=localhost 
ENV REDIS_PORT=6379  
ENV FLASK_APP=payoneer.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:80/ || exit 1
