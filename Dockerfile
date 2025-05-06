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