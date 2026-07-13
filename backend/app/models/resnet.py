import torch.nn as nn
from torchvision.models import (
    resnet18,
    ResNet18_Weights
)


def get_model(num_classes):

    model = resnet18(
        weights=ResNet18_Weights.DEFAULT
    )

    # Freeze all layers
    for param in model.parameters():
        param.requires_grad = False

    # Unfreeze last residual block (Fine Tuning)
    for param in model.layer4.parameters():
        param.requires_grad = True

    # Replace classifier
    in_features = model.fc.in_features

    model.fc = nn.Linear(
        in_features,
        num_classes
    )

    # Train classifier
    for param in model.fc.parameters():
        param.requires_grad = True

    return model