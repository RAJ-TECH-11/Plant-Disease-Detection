import torch
import torch.nn as nn
import torch.optim as optim

from tqdm import tqdm

from app.data.dataloader import (
    train_loader,
    val_loader,
    num_classes
)

from app.models.resnet import get_model


# -----------------------------------
# Device
# -----------------------------------

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Device: {device}")


# -----------------------------------
# Model
# -----------------------------------

model = get_model(num_classes).to(device)


# -----------------------------------
# Loss Function
# -----------------------------------

criterion = nn.CrossEntropyLoss()


# -----------------------------------
# Optimizer
# -----------------------------------

optimizer = optim.Adam(
    filter(lambda p: p.requires_grad, model.parameters()),
    lr=0.0001
)


# -----------------------------------
# Training Settings
# -----------------------------------

num_epochs = 5

best_val_accuracy = 0


# ===================================
# Training Loop
# ===================================

for epoch in range(num_epochs):

    model.train()

    running_loss = 0.0

    correct = 0
    total = 0

    for images, labels in tqdm(
        train_loader,
        desc=f"Epoch {epoch+1}/{num_epochs}",
        unit="batch"
    ):

        images = images.to(device)
        labels = labels.to(device)

        # Remove old gradients
        optimizer.zero_grad()

        # Forward Pass
        outputs = model(images)

        # Calculate Loss
        loss = criterion(outputs, labels)

        # Backpropagation
        loss.backward()

        # Update Weights
        optimizer.step()

        running_loss += loss.item()

        _, predicted = torch.max(outputs, 1)

        total += labels.size(0)

        correct += (predicted == labels).sum().item()

    train_loss = running_loss / len(train_loader)
    train_accuracy = 100 * correct / total

    # ===================================
    # Validation
    # ===================================

    model.eval()

    val_correct = 0
    val_total = 0

    with torch.no_grad():

        for images, labels in val_loader:

            images = images.to(device)
            labels = labels.to(device)

            outputs = model(images)

            _, predicted = torch.max(outputs, 1)

            val_total += labels.size(0)

            val_correct += (predicted == labels).sum().item()

    val_accuracy = 100 * val_correct / val_total

    # ===================================
    # Save Best Model
    # ===================================

    if val_accuracy > best_val_accuracy:

        best_val_accuracy = val_accuracy

        torch.save(
            model.state_dict(),
            "saved_models/resnet_best_model.pth"
        )

    # ===================================
    # Print Results
    # ===================================

    print("\n" + "=" * 50)

    print(f"Epoch              : {epoch+1}/{num_epochs}")

    print(f"Train Loss         : {train_loss:.4f}")

    print(f"Train Accuracy     : {train_accuracy:.2f}%")

    print(f"Validation Accuracy: {val_accuracy:.2f}%")

    print(f"Best Validation    : {best_val_accuracy:.2f}%")

    print("=" * 50)