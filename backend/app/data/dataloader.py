from pathlib import Path

from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader

from app.data.transforms import train_transforms, val_transforms

# Project Root
BASE_DIR = Path(__file__).resolve().parents[3]

train_path = BASE_DIR / "dataset" / "train"
valid_path = BASE_DIR / "dataset" / "valid"
test_path = BASE_DIR / "dataset" / "test"

# Dataset
train_dataset = ImageFolder(
    root=train_path,
    transform=train_transforms
)

val_dataset = ImageFolder(
    root=valid_path,
    transform=val_transforms
)

test_dataset = ImageFolder(
    root=test_path,
    transform=val_transforms
)

# DataLoader
train_loader = DataLoader(
    train_dataset,
    batch_size=32,
    shuffle=True
)

val_loader = DataLoader(
    val_dataset,
    batch_size=32,
    shuffle=False
)

test_loader = DataLoader(
    test_dataset,
    batch_size=32,
    shuffle=False
)

# Classes
class_names = train_dataset.classes
num_classes = len(class_names)