from fastapi import FastAPI
from pydantic import BaseModel
from model.model import predict_pipeline
from model.model import __version__ as model_version


app = FastAPI()


class TextIn(BaseModel):
    text: str


class PredictionOut(BaseModel):
    language: str


@app.get("/")
def home():
    return {"health_check": "OK", "model_version": model_version}


@app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    language = predict_pipeline(payload.text)
    return {"language": language}

# Docker build image : docker build -t language-detection-app .

# Run image = docker run -p 80:80 language-detection-app

# add requirements file = pip freeze > requirements.text     

# uvicorn main:app --reload