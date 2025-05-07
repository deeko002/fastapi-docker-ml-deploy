# 🚀 ML Model Deployment with FastAPI & Docker

A full-stack machine learning deployment pipeline built from scratch. This project trains a classification model using synthetic data, wraps it in a FastAPI REST API for inference, and containerizes the service using Docker for scalable production deployment.
---

## 📦 Project Overview

This application demonstrates the full lifecycle of a containerized machine learning system:

- ✅ Synthetic data generation
- ✅ Model training and persistence with `joblib`
- ✅ RESTful prediction API using **FastAPI**
- ✅ Containerization using **Docker**
- ✅ Endpoint testing with `curl`

---

## 🧠 ML Stack Used

- **FastAPI** – lightweight Python web framework for APIs  
- **scikit-learn** – used for model training  
- **joblib** – to save and load the trained model  
- **Docker** – containerization for portability  
- **pandas** – data manipulation  
- **uvicorn** – ASGI server to run FastAPI

---

## 🔧 Setup Instructions

### 1. Create and activate virtual environment

```bash
python -m venv venv
# On Unix/macOS
source venv/bin/activate
# On Windows
call venv\Scripts\activate.bat
```

### 2. Define dependencies

Create `requirements.in` with:

```
fastapi
uvicorn
pandas
scikit-learn
joblib
python-multipart
```

Then run:

```bash
pip install pip-tools
pip-compile requirements.in
pip install -r requirements.txt
```

---

## 🛠️ Usage

### 1. Generate data

```bash
python generate_data.py train.csv 2000
python generate_data.py test.csv 20
```

### 2. Train model

```bash
python generate_model.py
```

This saves a trained model to `model.pkl`.

### 3. Run FastAPI server

```bash
uvicorn app:app --reload
```

---

## 🐳 Docker Setup

### 1. Build Docker image

```bash
docker build -t python-ds-container .
```

### 2. Run Docker container

```bash
docker run -p 8000:8000 python-ds-container
```

---

## 🧪 API Testing (via `curl`)

If you're on Windows, use Git Bash or WSL.

```bash
curl -X POST http://localhost:8000/predict/ \
  -H "Content-Type: multipart/form-data" \
  -F "file=@test.csv"
```

Expected output:

```json
{"predictions":[1,0,1,0,...]}
```

> ⚠️ Remove the label column from `test.csv` before uploading, or prediction may fail.

---

## 📂 File Structure

```
├── app.py                # FastAPI app
├── model.pkl             # Trained ML model
├── Dockerfile            # Container instructions
├── generate_data.py      # Generates train/test CSVs
├── generate_model.py     # Trains and saves model
├── requirements.in
├── requirements.txt
└── .gitignore
```

---

## 🧠 What I Learned

- Converting notebooks to production-ready scripts
- Containerizing machine learning APIs
- Structuring clean Python APIs for inference
- Using FastAPI for rapid prototyping
- Reproducible environments with pip-tools

---

## 👨‍💻 Author

**Tarun Kumar Deekonda**  
MSBA Candidate @ UMN Carlson  
[GitHub](https://github.com/deeko002) | [LinkedIn](https://linkedin.com/in/tarunkumardeekonda)

---

## 📜 License

MIT License
