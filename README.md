# Chest Cancer Classification Project

This repository contains an end-to-end deep learning project for chest cancer classification using transfer learning with the VGG-16 model. The project includes a complete MLOps pipeline, covering data versioning, experiment tracking, continuous integration, and deployment. An interactive front end was built to enable real-time inferencing, deployed on Azure via Docker containers. This README outlines the tools and technologies used, setup instructions, and workflow steps.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Project Workflow](#project-workflow)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Acknowledgments](#acknowledgments)

---

## Project Overview

This project focuses on classifying chest cancer images using a pre-trained VGG-16 model, optimized for medical imaging. The project showcases a robust MLOps setup, enabling reproducible experiments, version control, and streamlined deployment. The front-end interface allows users to upload images and receive real-time predictions.

## Technologies Used

- **Python & Flask** - Core language for backend and inference server
- **MLflow** - For experiment tracking and parameter tuning
- **DVC (Data Version Control)** - Manages data and model versioning for reproducibility
- **GitHub Actions** - Automates continuous integration (CI) and continuous deployment (CD)
- **Docker** - Containerizes the application for portability and scalability
- **Azure** - Cloud platform for deployment
- **Tableau** - (Optional) For additional data visualization if desired

## Project Workflow

1. **Data Preprocessing and Versioning**:
   - Data is cleaned, transformed, and versioned using DVC for consistent results across environments.

2. **Model Training**:
   - A VGG-16 model is fine-tuned for chest cancer classification.
   - MLflow is used to track experiments, hyperparameters, and metrics to evaluate model performance.

3. **Continuous Integration (CI/CD)**:
   - GitHub Actions automates testing and deployment, ensuring a smooth development cycle.
   - Each commit triggers tests, and the latest model and code are deployed to Azure.

4. **Deployment**:
   - The application is containerized with Docker, ensuring consistency across environments.
   - Deployed on Azure for accessible, scalable inferencing.

5. **Interactive Front End**:
   - A user-friendly front end allows users to upload images and receive predictions in real-time.
   - Flask handles inferencing requests, serving the model and returning predictions to the front end.

## Setup Instructions

### Prerequisites

- Python 3.x
- Docker
- Azure Account
- DVC, GitHub Actions, and MLflow installed and configured
- Azure CLI for deployment to Azure

### Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/chest-cancer-classification.git
   cd chest-cancer-classification
   ```
2. **Install Python Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Initialize DVC:**
   Configure DVC to track data and models. Ensure dvc remote is set up to store versioned files.
   
   ```bash
   dvc init
   dvc remote add -d myremote <path-to-your-remote-storage>
   ```
4. **Run MLflow:**
   Start MLflow to track experiment parameters and metrics.
   ```bash
   mlflow ui```
5. **Setup Docker:**
   Build and run the Docker container.
   ```bash
   docker build -t chest-cancer-app .
   docker run -p 5000:5000 chest-cancer-app```
6. **Deploy to Azure:**
   Follow Azure CLI steps to deploy the Docker container on Azure.

**Setting Up GitHub Actions**
   Configure the .github/workflows/main.yml file to trigger automated tests and deploy on push events.

## Usage
1. **Running Locally:**
   Run the Flask application to start the interactive front end.
   ```bash
   python app.py```

## Project Structure
```bash
├── data/                 # Dataset and DVC files
├── models/               # Model files tracked by DVC
├── app.py                # Flask application for inferencing
├── requirements.txt      # Python dependencies
├── Dockerfile            # Docker configuration
├── .github/workflows/    # GitHub Actions workflows for CI/CD
├── README.md             # Project documentation
└── ...

```
## Acknowledgments
1. MLflow and DVC for providing robust tools for version control and experiment tracking.
2. Azure for cloud services that make deployment accessible and scalable.
3. GitHub Actions for automating CI/CD, ensuring streamlined development and deployment.
