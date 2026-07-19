# 🌿 Plant Disease Detection using Deep Learning

An AI-powered web application that detects plant leaf diseases from images using Deep Learning.

The project uses **Transfer Learning with ResNet18**, a **FastAPI backend**, and a **React frontend** to provide real-time disease prediction along with confidence score, disease description, symptoms, and prevention tips.

---

## 🚀 Live Demo

**Frontend:** https://plant-disease-detection-khaki.vercel.app

**Backend API:** https://plant-disease-detection-b9ez.onrender.com

**API Docs:** https://plant-disease-detection-b9ez.onrender.com/docs

---

## 📸 Screenshots

> Add screenshots here

- Home Page
- Upload Image
- Prediction Result
- Swagger API

---

# ✨ Features

- Upload plant leaf images
- Detect disease using Deep Learning
- Confidence score
- Top 3 predictions
- Disease description
- Symptoms
- Prevention tips
- FastAPI REST API
- React + Tailwind UI
- Responsive interface

---

# 🛠 Tech Stack

## Deep Learning

- PyTorch
- Torchvision
- ResNet18 (Transfer Learning)
- Custom CNN
- Transfer Learning
- Fine Tuning

## Backend

- FastAPI
- Uvicorn
- Pydantic

## Frontend

- React
- Vite
- Tailwind CSS
- Axios

## Others

- Pillow
- NumPy
- tqdm

---

# 🧠 Deep Learning Concepts Covered

- Image Classification
- CNN
- Transfer Learning
- Fine Tuning
- Data Augmentation
- Image Normalization
- Cross Entropy Loss
- Adam Optimizer
- Backpropagation
- Model Evaluation
- Model Saving & Loading
- Inference Pipeline

---

# 📂 Project Structure

```text
Plant-Disease-Detection
│
├── backend
│   ├── app
│   │   ├── data
│   │   ├── models
│   │   ├── schemas
│   │   ├── predict.py
│   │   ├── train.py
│   │   ├── train_resnet.py
│   │   ├── evaluate.py
│   │   └── disease_info.json
│   │
│   ├── saved_models
│   │   ├── best_model.pth
│   │   └── resnet_best_model.pth
│   │
│   ├── main.py
│   └── requirements.txt
│
├── frontend
│
├── dataset
│
└── scripts
```

---

# 📊 Model Comparison

| Model | Validation Accuracy |
|--------|--------------------:|
| Custom CNN | 51.94% |
| ResNet18 (Transfer Learning) | 83.82% |
| ResNet18 + Fine Tuning + Normalize | **99.17%** |

---

# 📈 Final Performance

| Metric | Score |
|---------|-------|
| Train Accuracy | 99.15% |
| Validation Accuracy | 99.17% |
| Test Accuracy | **99.13%** |

---

# 🔄 Workflow

```
Dataset

↓

Image Preprocessing

↓

Data Augmentation

↓

Transfer Learning (ResNet18)

↓

Fine Tuning

↓

Model Training

↓

Best Model Saved

↓

FastAPI Backend

↓

React Frontend

↓

Prediction
```

---

# 🖥 API Endpoints

## Home

```
GET /
```

Returns

```json
{
  "message": "Plant Disease Detection API Running"
}
```

---

## Predict Disease

```
POST /predict
```

Upload

```
multipart/form-data

file=image.jpg
```

Example Response

```json
{
  "prediction": {
    "disease": "Tomato Mosaic Virus",
    "confidence": 99.99
  },
  "top_predictions": [
    {
      "disease": "Tomato Mosaic Virus",
      "confidence": 99.99
    }
  ],
  "description": "...",
  "symptoms": [],
  "prevention": []
}
```

---

# ⚙️ Installation

## Clone

```bash
git clone https://github.com/RAJ-TECH-11/Plant-Disease-Detection.git

cd Plant-Disease-Detection
```

---

## Backend

```bash
cd backend

pip install -r requirements.txt

python -m uvicorn main:app --reload
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

---

# 📦 Deployment

Backend

- Render

Frontend

- Vercel

---

# 📚 Dataset

PlantVillage Dataset

The dataset contains healthy and diseased plant leaf images for multiple crop species.

Classes used: **15**

---

# 🎯 Future Improvements

- Support more plant species
- Mobile application
- Batch image prediction
- Explainable AI (Grad-CAM)
- Real-time camera prediction

---

# 👨‍💻 Author

**Raj Kewat**

GitHub: https://github.com/RAJ-TECH-11

---

# ⭐ If you found this project useful, consider giving it a star!