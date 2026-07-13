from app.data.dataloader import (
    train_loader,
    class_names,
    num_classes
)

print("Classes :", num_classes)

print()

print(class_names)

print()

images, labels = next(iter(train_loader))

print(images.shape)

print(labels.shape)

print(labels[:10])