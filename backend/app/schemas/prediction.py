from pydantic import BaseModel


class Prediction(BaseModel):
    disease: str
    confidence: float


class PredictionResponse(BaseModel):
    prediction: Prediction
    top_predictions: list[Prediction]
    description: str
    symptoms: list[str]
    prevention: list[str]