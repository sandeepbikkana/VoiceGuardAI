CI/CD Pipeline for ML Application (Task 11)
Overview

This repository demonstrates a CI/CD pipeline for an ML-style application, created to satisfy Task 11: CI/CD Pipeline for Deepfake Processing.

The focus is on automation and deployment, not on model complexity.
A minimal placeholder service is used to represent where deepfake inference logic would exist in a real system.

What This Project Demonstrates

Automated CI using GitHub Actions

Unit testing with PyTest

Code quality checks with Flake8

Dockerized application build

Deployment using a free-tier cloud service 

----Tech Stack----

Python 3.9

GitHub Actions

PyTest, Flake8

Docker

Ec2

Repository Structure
.
├── app.py
├── test_app.py
├── requirements.txt
├── Dockerfile
├── README.md
└── .github/workflows/ci.yml

----CI/CD Workflow----

1)The pipeline runs automatically on every push and pull request and performs:

2)Dependency installation

3)Test execution

4)Lint checks

5)Docker build

6)Application deployment

---Application Note---

This project does not implement actual deepfake processing.

The application acts as a placeholder inference service to demonstrate how a deepfake model would be:

1)Tested

2)Built

3)Containerized

4)Deployed using CI/CD

This reflects real-world ML DevOps workflows where pipelines are built independently of model logic.

----Deployment----

The application is deployed as a Web Service (Free Tier).

Live URL:

http://13.204.79.36:8000/health


---Screenshots---

Evidence of successful CI/CD execution and deployment.

GitHub Actions – CI Success

Deployment Logs

Service – Live

Live Application Response

References

GitHub Actions – Python CI

Docker CI/CD examples
