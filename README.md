# To-Do List Application

## Introduction
This repository contains the code for a To-Do List application. The application is built using EJS, Node.js, and Express.js, with additional tools and technologies integrated to enhance development and deployment processes.

## Technologies Used
- **EJS**: For templating and rendering views
- **Node.js**: JavaScript runtime for server-side development
- **Express.js**: Web framework for Node.js
- **Python**: Used for testing with pytest
- **Docker**: Containerization platform
- **Docker Swarm**: Container orchestration tool
- **GitHub Actions**: For CI/CD to automate Docker image build and push to Docker Hub

## Project Structure
- `app.js`: Main application file
- `views/`: Directory containing EJS files
- `node_modules/`: Directory containing npm packages
- `tests/`: Directory containing pytest test cases
- `Dockerfile`: Dockerfile to containerize the application
- `.github/workflows/main.yml`: GitHub Actions workflow file

## Setup Instructions

### Prerequisites
- Node.js and npm installed
- Docker installed
- Docker Hub account

### Running the Application Locally

1. Clone the repository on local machine cmnd prompt:

   git clone https://github.com/23024918/C270.git
   cd C270

2. Install dependencies:

   npm install

3. Start the application:
   node app.js

   Running the Application with Docker

1. Build the Docker image:
   docker build -t your-dockerhub-username/c270_app .

2. Run the Docker container:
   docker run -p 3000:3000 your-dockerhub-username/c270_app

   Running with Docker Swarm

1. Initialize Docker Swarm:
   docker swarm init

2. Deploy the stack:
   docker stack deploy --compose-file docker-compose.yml c270-stack

   Running Tests:
   
1. Install pytest:
   pip install pytest

2. Run the tests:
   pytest

   CI/CD CI/CD with GitHub Actions

   This repository uses GitHub Actions to automate the Docker image build and push process to Docker Hub. The workflow is defined in .github/workflows/main.yml.

   1. The workflow is triggered on every push to the main branch.
   2.  It builds the Docker image and pushes it to Docker Hub.
  
   This project is licensed under the MIT License - see the LICENSE file for details.
   You can now [create the README.md file](https://github.com/23024918/C270/new/main?filename=README.md) in your repository and paste the above content into it.



   




    

   

   

   

   
   



   
   



