# Counter Service

## Getting Started

## Introduction
Counter Service is a simple Flask web application designed to count the number of POST requests it receives and display this count on a GET request. The application is containerized using Docker, making it easy to deploy and scale. It is part of a DevOps exercise, demonstrating CI/CD practices using Azure DevOps.

# USAGE:

# POST- 
curl -X POST localhost:80


# GET
curl -X GET localhost:80

### Prerequisites
- Docker
- Python 3.8 or higher (if running locally without Docker)
- Access to an Azure DevOps account (for CI/CD pipeline)

### Installation

## Running with Docker:**
1. Clone the repository:
   ```sh
   git clone https://github.com/edenmor/counter-service.git
cd counter-service
docker build -t counter-service .
docker run -d -p 80:80 counter-service

CI/CD Pipeline
The CI/CD pipeline, defined in azure-pipelines.yml, automates the process of building, testing, and deploying the application. Upon a commit and push to the repository, the pipeline is triggered, ensuring that the application is always up-to-date in the production environment.

Deployment
The application is deployed on an AWS EC2 instance. The deployment process is handled by the CI/CD pipeline, which uses SSH to connect to the instance and deploy the Docker container.

