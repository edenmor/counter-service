Counter Service
Description
This repository contains the implementation of the Counter Service, a Flask web application designed to count POST requests and display the count on a GET request. Below is a summary of the key changes and implementations:

Python Flask Web Service: Developed a Flask application to count POST requests and display the count on a GET request.
Dockerization: Containerized the Flask application using Docker for easy deployment and scalability.
CI/CD Pipeline: Configured an Azure DevOps pipeline for continuous integration and deployment, automating the build, test, and deployment processes.
Testing: Included basic tests to ensure the application functionality, especially the counting mechanism.
Documentation: Added this README.md file detailing the setup, usage, and other relevant information about the project.
Additional Considerations:

The counter resets to zero upon each new deployment as the current implementation does not include persistent storage.
Deployment Methods
1. Azure Pipelines
To deploy using Azure Pipelines:

Ensure you have the azure-pipelines.yaml file in the root of your repository. This file defines the CI/CD pipeline for automating the build, test, and deployment processes.
Set up a private EC2 instance as an agent for your builds.
Commit your changes to trigger the pipeline.
2. Argo CD
For deployment using Argo CD:

Use the following files:
deployment.yaml: Defines the deployment of the Flask application.
service.yaml: Configures the service to expose the Flask application.
Attach the dev file to Argo CD with the deployment and service YAMLs.
Configure Argo CD to manage and monitor the deployment of your application.
3. GitHub Actions
To deploy using GitHub Actions:

Ensure you have workflow files in the .github/workflows directory.
Define your workflows in the YAML files located in this directory.
Push your changes to trigger the GitHub Actions workflows for building, testing, and deploying the application.
