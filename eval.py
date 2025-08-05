# Copyright (C) 2025 Colin Damon
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
SpotR model evaluation script

Usage:
    Edit the following variables at the top of this script to match
    your evaluation setup:
        - TEST_CSV: Path to your test CSV file
        - IMAGE_DIR: Path to the image directory
        - NUM_CLASSES: Number of classes in your dataset
        - MODEL_NAME: Model architecture
            (e.g. 'resnet101v1', 'resnet50v1', etc.)
        - WEIGHTS_PATH: Path to the trained model weights

    Then run the script with:
        python train.py

The script will evaluate your trained model on the test set, print
accuracy, and show a classification report. To additionally output
a confusion matrix, uncomment the final two lines in this script.

To use different datasets, models, or weight files, edit the
relevant variables and rerun the script.
"""

import torch
import torch.nn as nn
from torchvision import models
from data import StanfordCarsDataset, get_val_transforms, get_dataloader
from sklearn.metrics import classification_report

TEST_CSV = "dataset/train1/test1.csv"
IMAGE_DIR = "dataset/"
NUM_CLASSES = 196
MODEL_NAME = "resnet101v1"
WEIGHTS_PATH = "models/spotr_weights.pth"

print("LOADING DEVICE, DATASET, and DATALOADER...")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
test_dataset = StanfordCarsDataset(TEST_CSV, IMAGE_DIR, transform=get_val_transforms())
test_loader = get_dataloader(test_dataset, batch_size=32, shuffle=False)

print("LOADING MODEL and WEIGHTS...")
if MODEL_NAME == "resnet50v1":
    model = models.resnet50(weights='IMAGENET1K_V1')
    model.fc = nn.Linear(model.fc.in_features, NUM_CLASSES)
elif MODEL_NAME == "resnet50v2":
    model = models.resnet50(weights='IMAGENET1K_V2')
    model.fc = nn.Linear(model.fc.in_features, NUM_CLASSES)
elif MODEL_NAME == "resnet101v1":
    model = models.resnet101(weights='IMAGENET1K_V1')
    model.fc = nn.Linear(model.fc.in_features, NUM_CLASSES)
elif MODEL_NAME == "resnet101v2":
    model = models.resnet101(weights='IMAGENET1K_V2')
    model.fc = nn.Linear(model.fc.in_features, NUM_CLASSES)
else:
    raise ValueError("Unknown model name")
model.load_state_dict(torch.load(WEIGHTS_PATH, map_location=device))
model = model.to(device)
model.eval()

print("ENTERING EVALUATION LOOP...")
correct, total = 0, 0
all_preds, all_labels = [], []
with torch.no_grad():
    for images, labels in test_loader:
        images, labels = images.to(device), labels.to(device)
        outputs = model(images)
        _, preds = torch.max(outputs, 1)
        correct += (preds == labels).sum().item()
        total += labels.size(0)
        all_preds.extend(preds.cpu().numpy())
        all_labels.extend(labels.cpu().numpy())
test_acc = correct / total

print("EVALUATION FINISHED!\n")
print(f"Test Accuracy: {test_acc:.6f}")
print(classification_report(all_labels, all_preds))
#print("Confusion Matrix:")
#print(confusion_matrix(all_labels, all_preds))
