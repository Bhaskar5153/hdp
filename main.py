import os
import sys

from fastapi import FastAPI
from pydantic import BaseModel

import pandas as pd
import pickle


class HeartDiseasePredictionRequest(BaseModel):
    male: int
    age: int
    education: int
    currentSmoker: int
    cigsPerDay: int
    BPMeds: int
    prevalentStroke: int
    prevalentHyp: int
    diabetes: int
    totChol: int
    sysBP: int
    diaBP: int
    BMI: float
    heartRate: float
    glucose: float


# from pydantic import BaseModel

# class PredictionResponse(BaseModel):
#     prediction: int



# initialize the app

app = FastAPI()

model_path = r"C:\Users\Priya Bhaskar\practice_ml_projects\heart_disease_prediction\hdp\notebooks\artifacts\logistic_regression_chd_model.pkl"

# load the model

with open(file=model_path, mode='rb') as f:
    model = pickle.load(f)


@app.get("/")
def root():
    return {"message": "Welcome to Heart Disease Prediction"}

@app.post("/predict", response_model=None)
def predict(request: HeartDiseasePredictionRequest):
    df = pd.DataFrame([request.model_dump()])
    prediction = int(model.predict(df)[0])
    return {"CHD_Prediction": prediction}


