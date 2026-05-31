from fastapi import FastAPI
from pydantic import BaseModel
# import pickle
import pandas as pd
import joblib

# load model
with open('model.pkl', 'rb') as file:
    model = joblib.load(file)

app = FastAPI()

# define input schema
class InputData(BaseModel):
    age: int
    workclass: str
    education: str
    marital_status: str
    occupation: str
    relationship: str
    race: str
    gender: str
    capital_gain: int
    capital_loss: int
    hours_per_week: int
    native_country: str


@app.get('/')
def welcome_message():
    return {"message": "Welcome to Model API"}


@app.post('/predict')
def prediction(data: InputData):

    input_data = pd.DataFrame([data.dict()])

    pred = model.predict(input_data)

    return {"prediction": str(pred[0])} 