import joblib
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import nest_asyncio
from typing import Optional
import pandas as pd

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:4200", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)

class InputData(BaseModel):
    Sadness: Optional[str]
    Euphoric: Optional[str]
    Exhausted: Optional[str]
    Sleep_dissorder: Optional[str]
    Mood_Swing: Optional[float]
    Suicidal_thoughts: Optional[float]
    Anorxia: Optional[float]
    Authority_Respect: Optional[float]
    Try_Explanation: Optional[float]
    Aggressive_Response: Optional[float]
    Ignore_Move_On: Optional[float]
    Nervous_Break_down: Optional[float]
    Admit_Mistakes: Optional[float]
    Overthinking: Optional[float]
    Sexual_Activity: Optional[float]
    Concentration: Optional[float]
    Optimisim: Optional[float]
  
modelo = joblib.load('MentalDisorders.pkl')

@app.post("/predict/")
async def predict(data: InputData):
    features = {
        'Sadness': [data.Sadness], 
        'Euphoric': [data.Euphoric], 
        'Exhausted': [data.Exhausted], 
        'Sleep dissorder': [data.Sleep_dissorder],
        'Mood Swing': [data.Mood_Swing], 
        'Suicidal thoughts': [data.Suicidal_thoughts], 
        'Anorxia': [data.Anorxia],
        'Authority Respect': [data.Authority_Respect], 
        'Try-Explanation': [data.Try_Explanation], 
        'Aggressive Response': [data.Aggressive_Response],
        'Ignore & Move-On': [data.Ignore_Move_On], 
        'Nervous Break-down': [data.Nervous_Break_down], 
        'Admit Mistakes': [data.Admit_Mistakes],
        'Overthinking': [data.Overthinking], 
        'Sexual Activity': [data.Sexual_Activity], 
        'Concentration': [data.Concentration],
        'Optimisim': [data.Optimisim]
    }

    df = pd.DataFrame(features)

    prediction = modelo.predict(df)[0]
    return {"answer": prediction}

if __name__ == "__main__":
    nest_asyncio.apply() 
    uvicorn.run(app, host="0.0.0.0", port=8000)
