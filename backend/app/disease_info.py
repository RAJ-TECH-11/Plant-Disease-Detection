import torch
from PIL import Image
from torchvision import transforms

from app.models.cnn import PlantDiseaseCNN
from app.data.dataloader import class_names, num_classes
from app.disease_info import DISEASE_INFO


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


# -----------------------------
# Load Model
# -----------------------------

model = PlantDiseaseCNN(num_classes=num_classes)

model.load_state_dict(
    torch.load(
        "saved_models/best_model.pth",
        map_location=device
    )
)

model.to(device)

model.eval()


# -----------------------------
# Image Transform
# -----------------------------

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
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

    DISEASE_INFO = {

    "Tomato_Late_blight": {

        "description":
        "A fungal disease that spreads rapidly in humid weather.",

        "symptoms": [

            "Dark brown lesions",

            "White fungal growth",

            "Leaves dry quickly"

        ],

        "prevention": [

            "Remove infected leaves",

            "Avoid overhead watering",

            "Use fungicide"

        ]

    },

    "Tomato_healthy": {

        "description":
        "The plant appears healthy.",

        "symptoms": [

            "Healthy green leaves"

        ],

        "prevention": [

            "Continue proper irrigation",

            "Regular monitoring"

        ]

    }

}