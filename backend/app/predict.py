import json
from pathlib import Path

import torch
from PIL import Image
from torchvision import transforms

# Resolve paths relative to this file's location
BASE_DIR = Path(__file__).resolve().parents[1]  # backend/ directory

from app.models.resnet import get_model

# Hardcoded class names (sorted alphabetically, matching ImageFolder order)
# This avoids importing dataloader.py which requires the training dataset on disk
class_names = [
    "Pepper__bell___Bacterial_spot",
    "Pepper__bell___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Tomato_Bacterial_spot",
    "Tomato_Early_blight",
    "Tomato_Late_blight",
    "Tomato_Leaf_Mold",
    "Tomato_Septoria_leaf_spot",
    "Tomato_Spider_mites_Two_spotted_spider_mite",
    "Tomato__Target_Spot",
    "Tomato__Tomato_YellowLeaf__Curl_Virus",
    "Tomato__Tomato_mosaic_virus",
    "Tomato_healthy",
]
num_classes = len(class_names)


# -----------------------------
# Device
# -----------------------------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


# -----------------------------
# Load Model
# -----------------------------
model = get_model(num_classes)

model.load_state_dict(
    torch.load(
        BASE_DIR / "saved_models" / "resnet_best_model.pth",
        map_location=device
    )
)

model.to(device)
model.eval()


# -----------------------------
# Load Disease Information
# -----------------------------
with open(BASE_DIR / "app" / "disease_info.json", "r") as file:
    DISEASE_INFO = json.load(file)


# -----------------------------
# Image Transform
# -----------------------------
transform = transforms.Compose([

    transforms.Resize((224,224)),

    transforms.ToTensor(),

    transforms.Normalize(
        mean=[0.485,0.456,0.406],
        std=[0.229,0.224,0.225]
    )

])


# -----------------------------
# Prediction Function
# -----------------------------
def predict(image_path):

    image = Image.open(image_path).convert("RGB")

    image = transform(image)

    image = image.unsqueeze(0).to(device)

    with torch.no_grad():

        outputs = model(image)

        probabilities = torch.softmax(outputs, dim=1)

        top_probs, top_indices = torch.topk(probabilities, k=3)

    predictions = []

    for prob, idx in zip(top_probs[0], top_indices[0]):

        predictions.append({
            "disease": class_names[idx.item()],
            "confidence": round(prob.item() * 100, 2)
        })

    best_prediction = predictions[0]

    info = DISEASE_INFO.get(best_prediction["disease"], {})

    return {

        "prediction": best_prediction,

        "top_predictions": predictions,

        "description": info.get("description", ""),

        "symptoms": info.get("symptoms", []),

        "prevention": info.get("prevention", [])

    }