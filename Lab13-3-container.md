# Lab 13-3: Building a Containerized Data Science Application

## Overview

In this lab, you will build a containerized FastAPI application for data science model deployment. The application will provide a REST API endpoint for making predictions using a machine learning model.

## Objectives

By the end of this lab, you will be able to:
1. Set up a FastAPI application for model deployment
2. Create a Docker container for Python applications
3. Build and test a containerized machine learning application
4. Use curl for API testing

## Prerequisites

- Python 3.11+
- Docker installed on your machine
- Basic understanding of FastAPI and Docker

## Part 1: Setup Lab folder

1. Download the lab file (`lab13-3-container.zip`), unzip it
2. Open the lab folder in VS Code (or other similar IDEs).
3. Review `generate_data.py`
    - This script will generate a training or testing dataset.
4. Review `generate_model.py`
    - This script will train a machine learning model using `train.csv` and save the resultant model to `model.pkl`.
5. Review `.gitignore`
    - This file will specify which files and directories should be ignored by Git.
    - You can usually ask ChatGPT or other AI tools to generate a `.gitignore` file for you.

## Part 2: Set up python environment

1. create a virtual environment using `python -m venv venv`
2. activate the virtual environment
```bash
source venv/bin/activate  # On Unix/macOS
# or
call venv\Scripts\activate.bat  # On Windows
```
3. Create a `requirements.in` file

Collect the dependencies from the code and include them in the `requirements.in` file (no version needed). 

```
fastapi
uvicorn
pandas
scikit-learn
joblib
python-multipart
```

4. Install `pip-tools`

We will use pip-tools to generate the requirements.txt file to fix the versions of the dependencies. It also generates indirect dependencies.
```bash
pip install pip-tools
```

5. Generate `requirements.txt`:
```bash
pip-compile requirements.in
```

6. Install the dependencies:
```bash
pip install -r requirements.txt
```

If you need to add new dependencies, you can add them to the `requirements.in` file and run `pip-compile` again.


## Part 3: Data Generation

1. Create `generate_data.py` to generate synthetic data for training and testing:
```bash
python generate_data.py train.csv 2000
python generate_data.py test.csv 20
```

## Part 4: Model Training

The purpose of this piece of code is to train a model using training data and save the model. 

The code could be based your model development using (jupyter notebook). We convert such code to pure python and optimize it for production, by:

- remove **dead code** (e.g. visualization, random exploration codes, model testing code)
- add code to save the trained model to a pickle file (`model.pkl`).
- add exception handling
- add comments
- add abstraction (functions, __main__ etc) 

1. Generate and save your model:
```bash
python generate_model.py
```

## Part 5: Add FastAPI Application

1. Create `app.py`:

Add the following codes:
- Set up a FastAPI application
- Load the trained model at startup
- Create a `/predict/` endpoint that accepts CSV file uploads
- Return predictions in JSON format

```python
from fastapi import FastAPI, UploadFile, File
import pandas as pd
import joblib
import io

app = FastAPI()

# Load the model at startup
model = joblib.load('model.pkl')

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Read uploaded CSV file into pandas DataFrame
    contents = await file.read()
    df = pd.read_csv(io.BytesIO(contents))
    
    # Make predictions
    preds = model.predict(df)
    
    # Return predictions as a list
    return {"predictions": preds.tolist()}

```


## Part 6: Containerization

1. Create a `Dockerfile`:
   - Use an appropriate Python base image
   - Install dependencies from requirements.txt
   - Copy application files
   - Set up the entry point

```dockerfile
# choose the python version that matches your local environment
FROM python:3.11

WORKDIR /app

# Copy all necessary files
COPY app.py model.pkl requirements.txt ./

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to run FastAPI app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

2. Build and run your container:

Docker (or Docker Desktop) is required to be installed on your system for this step.  If you are doing this for the first time, it may take several minutes as it may need to download the base image.

```bash
docker build -t python-ds-container .

```

3. Run the container:
```bash
docker run -p 8000:8000 python-ds-container
```

## Part 7: Testing FastAPI Application

1. Test the API using `curl`:

`curl` is a Linux command-line tool that lets your computer talk to other computers over the internet, specifically to request information from websites or services. It can be used to make HTTP requests.

> If the curl command is not available in your cmd Window, you can open a `Git Bash` terminal (available if you install Git for Windows), and try the command there.


```bash
# one line format, works in all terminals
curl -X POST http://localhost:8000/predict/ -H "Content-Type: multipart/form-data" -F "file=@test.csv"

# multi line format, only in bash terminals
curl -X POST http://localhost:8000/predict/ \
  -H "Content-Type: multipart/form-data" \
  -F "file=@test.csv"
```

2. Verify that we get a result like this:

> Note that because our generated test.csv has an extra label column, it will fail. 
> After you remove the label column from test.csv file, it will go through.

```json
{"predictions":[0,1,1,0,0,0,0,1,1,0,0,1,0,1,1,0,0,0,1,0]}
```

## Submission

1. Take a screen shot of the following command and output, and submit the screenshot (the image file).

```bash
git log --oneline --graph --all --pretty=format:"%h %ad %s"
```

2. Take a screenshot of the following command and output, and submit the screenshot (the image file). 
> if you're on windows, you can do this command using a `Git Bash` window.

Such as:

```bash
dir > ls -l
-rwxrw-r--+ 1 dexli dexli     30 Apr 26 22:47 activate-python.bat
-rwxrw-r--+ 1 dexli dexli     24 Apr 26 22:49 activate-python.sh
-rwxrw-r--+ 1 dexli dexli    671 Apr 27 00:26 app.py
-rwxrw-r--+ 1 dexli dexli    340 Apr 26 23:11 Dockerfile
```

3. Take a screenshot of your API testing command and results, and submit the screenshot (the image file).

```bash
(venv) C:\repos\python-ds-container>curl ....
result.....
```