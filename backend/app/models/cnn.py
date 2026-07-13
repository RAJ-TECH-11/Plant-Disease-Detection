import torch
import torch.nn as nn


class PlantDiseaseCNN(nn.Module):

    def __init__(self, num_classes=15):
        super().__init__()

        self.features = nn.Sequential(

            nn.Conv2d(
                in_channels=3,
                out_channels=32,
                kernel_size=3,
                padding=1
            ),

            nn.ReLU(inplace=True),

            nn.MaxPool2d(2),


            nn.Conv2d(
                32,
                64,
                kernel_size=3,
                padding=1
            ),

            nn.ReLU(inplace=True),

            nn.MaxPool2d(2),


            nn.Conv2d(
                64,
                128,
                kernel_size=3,
                padding=1
            ),

            nn.ReLU(inplace=True),

            nn.MaxPool2d(2)
        )


        self.pool = nn.AdaptiveAvgPool2d((1, 1))


        self.classifier = nn.Sequential(

            nn.Flatten(),

            nn.Linear(128, 256),

            nn.ReLU(inplace=True),

            nn.Dropout(0.5),

            nn.Linear(256, num_classes)
        )

    def forward(self, x):

        x = self.features(x)

        x = self.pool(x)

        x = self.classifier(x)

        return x