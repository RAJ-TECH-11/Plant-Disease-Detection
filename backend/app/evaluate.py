import torch
import torch.nn as nn

from app.models.resnet import get_model
from app.data.dataloader import (
    test_loader,
    num_classes
)


device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

model = get_model(num_classes)

model.load_state_dict(
    torch.load(
        "saved_models/resnet_best_model.pth",
        map_location=device
    )
)

model.to(device)

model.eval()


criterion = nn.CrossEntropyLoss()

running_loss = 0

correct = 0

total = 0


with torch.no_grad():

    for images, labels in test_loader:

        images = images.to(device)

        labels = labels.to(device)

        outputs = model(images)

        loss = criterion(outputs, labels)

        running_loss += loss.item()

        _, predicted = torch.max(outputs, 1)

        total += labels.size(0)

        correct += (predicted == labels).sum().item()


test_loss = running_loss / len(test_loader)

test_accuracy = 100 * correct / total


print("\n" + "=" * 50)

print(f"Test Loss     : {test_loss:.4f}")

print(f"Test Accuracy : {test_accuracy:.2f}%")

print("=" * 50)