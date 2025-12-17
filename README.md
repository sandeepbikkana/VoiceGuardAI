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

Deployment using a free-tier cloud service (Render)

Tech Stack

Python 3.9

GitHub Actions

PyTest, Flake8

Docker

Render Web Service

Repository Structure
.
├── app.py
├── test_app.py
├── requirements.txt
├── Dockerfile
├── README.md
└── .github/workflows/ci.yml

CI/CD Workflow

The pipeline runs automatically on every push and pull request and performs:

Dependency installation

Test execution

Lint checks

Docker build

Application deployment

Application Note

This project does not implement actual deepfake processing.

The application acts as a placeholder inference service to demonstrate how a deepfake model would be:

Tested

Built

Containerized

Deployed using CI/CD

This reflects real-world ML DevOps workflows where pipelines are built independently of model logic.

Deployment

The application is deployed as a Render Web Service (Free Tier).

Live URL:
https://voiceguardai.onrender.com

Free-tier instances may sleep after inactivity, which is acceptable for demo purposes.

Screenshots

Evidence of successful CI/CD execution and deployment.

GitHub Actions – CI Success

Render Deployment Logs

Render Service – Live

Live Application Response

References

GitHub Actions – Python CI

Docker CI/CD examples

Render Web Services documentation
