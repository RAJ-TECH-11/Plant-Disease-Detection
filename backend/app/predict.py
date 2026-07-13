import json
import torch
from PIL import Image
from torchvision import transforms

from app.models.resnet import get_model
from app.data.dataloader import class_names, num_classes


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
        "saved_models/resnet_best_model.pth",
        map_location=device
    )
)

model.to(device)
model.eval()


# -----------------------------
# Load Disease Information
# -----------------------------
with open("app/disease_info.json", "r") as file:
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