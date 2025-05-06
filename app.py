from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import pandas as pd
import joblib
import io
import traceback

app = FastAPI()

# Load the model at startup
model = joblib.load('model.pkl')

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        df = pd.read_csv(io.BytesIO(contents))

        # Drop any columns not seen during training
        expected_features = model.feature_names_in_
        df = df[expected_features]  # filter to known features only

        print("📄 Cleaned CSV HEAD:\n", df.head())

        preds = model.predict(df)
        return {"predictions": preds.tolist()}
    
    except Exception as e:
        import traceback
        traceback.print_exc()
        return JSONResponse(status_code=500, content={"error": str(e)})

