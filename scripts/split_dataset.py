import random
import shutil
from pathlib import Path

# ----------------------------
# Configuration
# ----------------------------
random.seed(42)

SOURCE_DIR = Path("dataset/PlantVillage")

TRAIN_DIR = Path("dataset/train")
VALID_DIR = Path("dataset/valid")
TEST_DIR = Path("dataset/test")

TRAIN_RATIO = 0.8
VALID_RATIO = 0.1
TEST_RATIO = 0.1


def create_directories():
    """Create train/valid/test directories."""
    for split_dir in [TRAIN_DIR, VALID_DIR, TEST_DIR]:
        split_dir.mkdir(parents=True, exist_ok=True)


def split_class(class_dir):
    class_name = class_dir.name

    images = list(class_dir.glob("*"))

    random.shuffle(images)

    total = len(images)

    train_end = int(total * TRAIN_RATIO)
    valid_end = train_end + int(total * VALID_RATIO)

    train_images = images[:train_end]
    valid_images = images[train_end:valid_end]
    test_images = images[valid_end:]

    for split_dir, split_images in [
        (TRAIN_DIR, train_images),
        (VALID_DIR, valid_images),
        (TEST_DIR, test_images)
    ]:

        destination = split_dir / class_name
        destination.mkdir(parents=True, exist_ok=True)

        for image in split_images:
            shutil.copy2(image, destination / image.name)

    print(
        f"{class_name:<40} "
        f"Train: {len(train_images):4} | "
        f"Valid: {len(valid_images):4} | "
        f"Test: {len(test_images):4}"
    )


def main():

    create_directories()

    class_folders = sorted(
        [folder for folder in SOURCE_DIR.iterdir() if folder.is_dir()]
    )

    print(f"Found {len(class_folders)} classes\n")

    for class_folder in class_folders:
        split_class(class_folder)

    print("\nDataset split completed successfully.")


if __name__ == "__main__":
    main()