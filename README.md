# Counter Service

## Getting Started

## Introduction
Counter Service is a simple Flask web application designed to count the number of POST requests it receives and display this count on a GET request. The application is containerized using Docker, making it easy to deploy and scale. It is part of a DevOps exercise, demonstrating CI/CD practices using Azure DevOps.


# POST- 
curl -X POST localhost:80
curl -X POST <ec2-address>/

# GET
curl -X GET localhost:80
curl -X GET <ec2-adresss>

### Prerequisites
- Docker
- Python 3.8 or higher (if running locally without Docker)
- Access to an Azure DevOps account (for CI/CD pipeline)

### Installation

## Running with Docker:**
1. Clone the repository:
   ```sh
   git clone https://github.com/edenmor/counter-service.git
```
cd counter-service
docker build -t counter-service .
docker run -d -p 80:80 counter-service
```


## Deployment

The application is deployed on an AWS EC2 instance. The deployment process is handled by the CI/CD pipeline, which uses SSH to connect to the instance and deploy the Docker container.

## Usage
- **Increment the counter**: Send a POST request to `/`.
- **View the counter**: Send a GET request to `/`.

## CI/CD Pipeline
The CI/CD process, defined in `azure-pipelines.yml`, includes automated stages for building, testing, and deploying the application. The pipeline is triggered by commits to the `main` branch in the GitHub repository.

## Deployment
The application is deployed on an AWS EC2 instance, facilitated by the CI/CD pipeline. The pipeline uses SSH to deploy the Docker container in the production environment.
