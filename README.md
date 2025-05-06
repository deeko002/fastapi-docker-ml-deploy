# Python Data Science Container

Author: De Liu (2025)

A containerized FastAPI application for data science model deployment. This project provides a REST API endpoint for making predictions using a pre-trained machine learning model.

Prepared for MSBA 6331 Big Data Analytics

## Features

- FastAPI-based REST API server
- Model prediction endpoint for CSV file uploads
- Containerized deployment using Docker
- Pre-trained model included

## Prerequisites

- Docker and Docker Compose (for containerized deployment)
- Python 3.11+ (for local development)

## Setup Instructions

### Option 1: Using Docker (Recommended)

1. Build the Docker image:
```bash
docker build -t python-ds-container .
```

2. Run the container:
```bash
docker run -p 8000:8000 python-ds-container
```

3. View the FastAPI documentation:

Open a browser, and navigate to `http://localhost:8000/docs`.


4. Test the API

Suppose that you have generated a `test.csv` file using `generate_data.py`.

```bash
curl -X POST http://localhost:8000/predict/ \
  -H "Content-Type: multipart/form-data" \
  -F "file=@test.csv"
```

> `curl`: command-line tool for transferring data with URL syntax.

> If the curl command is not working on Windows, you can open a bash terminal, and try the command there.

### Option 2: Local Development

1. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Unix/macOS
# or
venv\Scripts\activate     # On Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Generate data:

Using the included code to generate a training or testing dataset.

```bash
# usage: python generate_data.py <filename> <num_samples>
python generate_data.py train.csv 2000
python generate_data.py test.csv 20
```

4. Generate model:

This script will train a machine learning model using `train.csv` and save the resultant model to `model.pkl`.

```bash
python generate_model.py
```

## Usage

The API provides a single endpoint for making predictions:

- POST `/predict/` - Accepts a CSV file and returns predictions

Example using curl:
```bash
curl -X POST http://localhost:8000/predict/ \
  -H "Content-Type: multipart/form-data" \
  -F "file=@test.csv"
```

## Project Structure

- `app.py` - Main FastAPI application
- `model.pkl` - Pre-trained machine learning model
- `generate_data.py` - Data generation script
- `generate_model.py` - Model training script
- `requirements.txt` - Python dependencies
- `Dockerfile` - Container configuration

## Development

The project uses pip-tools for dependency management. To update dependencies:

```bash
pip install pip-tools
pip-compile requirements.in
```

## License

MIT License