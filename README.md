CI/CD Pipeline for ML Application (Deepfake Pipeline Demo)
Overview

This repository demonstrates a CI/CD pipeline for an ML-style application, designed in the context of a deepfake processing system.

The focus of this project is CI/CD automation—including testing, linting, containerization, and deployment.
A minimal placeholder application is used instead of an actual deepfake model to keep the emphasis on DevOps practices.

Key Features

Automated CI using GitHub Actions

Unit testing with PyTest

Code quality checks using Flake8

Containerized build with Docker

Deployment using Render (Free Tier)

Tech Stack

Python 3.9

GitHub Actions

PyTest, Flake8

Docker

Render Web Service

Project Structure
.
├── app.py
├── test_app.py
├── requirements.txt
├── Dockerfile
├── README.md
└── .github/
    └── workflows/
        └── ci.yml

CI/CD Pipeline

The pipeline runs automatically on:

push

pull_request

Pipeline Steps

Checkout code

Setup Python

Install dependencies

Run unit tests

Run lint checks

Build Docker image

Deploy application

Application Description

The application exposes a lightweight API endpoint that represents an ML inference service.

Note:
The actual deepfake model logic is intentionally omitted. In a real system, this service would host a trained deepfake detection or generation model.

This approach reflects real-world ML DevOps workflows, where CI/CD pipelines are validated independently of model complexity.

Deployment

The application is deployed as a Render Web Service (Free Tier).

Docker-based deployment

Automatic port detection

Free-tier sleep behavior is acceptable for demo purposes

Live URL:
https://voiceguardai.onrender.com

Model Lifecycle (Conceptual)

In a production deepfake pipeline:

DVC would manage dataset and model versions

MLflow would track experiments and artifacts

These tools are referenced conceptually to maintain focus on CI/CD.

Evidence

Successful GitHub Actions CI runs

Docker build logs

Render deployment status and application logs

Live endpoint response

Screenshots are included in the submission.

References

GitHub Actions Python CI documentation

Docker CI/CD examples

Render Web Services documentation

Summary

This project successfully demonstrates a CI/CD pipeline suitable for ML and deepfake-style applications.
While the application logic is minimal, the pipeline design reflects production-grade DevOps practices and satisfies Task 11 requirements.
