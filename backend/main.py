import os
import shutil

from fastapi import (
    FastAPI,
    UploadFile,
    File,
    HTTPException
)
from fastapi.middleware.cors import CORSMiddleware

from app.predict import predict
from app.schemas.prediction import PredictionResponse


app = FastAPI(
    title="Plant Disease Detection API"
)

# Allow frontend origins (deployment + local dev)
frontend_url = os.environ.get("FRONTEND_URL", "")
allowed_origins = [
    "http://localhost:5173",
    "https://plant-disease-detection-khaki.vercel.app",
]
if frontend_url:
    allowed_origins.append(frontend_url)

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/")
def home():
    return {
        "message": "Plant Disease Detection API Running"
    }


@app.post(
    "/predict",
    response_model=PredictionResponse
)
async def predict_disease(file: UploadFile = File(...)):

    # Validate file
    if not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code=400,
            detail="Only image files are allowed."
        )

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    # Save uploaded image
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        result = predict(file_path)

    finally:
        # Delete uploaded image after prediction
        if os.path.exists(file_path):
            os.remove(file_path)

    return result