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
SpotR model training script

Usage:
    Edit the following variables at the top of this script to match
    your dataset and preferences:
        - TRAIN_CSV: Path to your training CSV file
        - VAL_CSV: Path to your validation CSV file
        - IMAGE_DIR: Path to the image directory
        - NUM_CLASSES: Number of classes in your dataset
        - MODEL_NAME: Model architecture 
            (e.g. 'resnet101v1', 'resnet50v1', etc.)
        - NUM_EPOCHS: Number of training epochs
        - optimizer/scheduler parameters

    Then run the script with:
        python train.py

The script will train a ResNet model on your dataset and save the
best weights (by validation accuracy) in the models/new_train/
directory by default.

To use different datasets, models, or hyperparameters, edit the
relevant variables and rerun the script.
"""

import os
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import models
from data import StanfordCarsDataset, get_train_transforms, get_val_transforms, get_dataloader

# Paths and Constants
TRAIN_CSV = "dataset/train1/train1.csv"
VAL_CSV = "dataset/train1/val1.csv"
IMAGE_DIR = "dataset/"
NUM_CLASSES = 196
MODEL_NAME = "resnet101v1"
NUM_EPOCHS = 10

print(f"DEVICE: {"cuda" if torch.cuda.is_available() else "cpu"}")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print("LOADING DATASETS/DATALOADERS...")
train_dataset = StanfordCarsDataset(TRAIN_CSV, IMAGE_DIR, transform=get_train_transforms())
val_dataset = StanfordCarsDataset(VAL_CSV, IMAGE_DIR, transform=get_val_transforms())
train_loader = get_dataloader(train_dataset, batch_size=32, shuffle=True)
val_loader = get_dataloader(val_dataset, batch_size=32, shuffle=False)

print(f"LOADING MODEL {MODEL_NAME}...")
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
model = model.to(device)

print("LOADING LOSS, OPTIMIZER, and SCHEDULER...")
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=1e-4)
scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=5, gamma=0.1)

print("ENTERING TRAINING/VALIDATION LOOP...")
best_val_acc = 0.0

for epoch in range(NUM_EPOCHS):
    # training
    model.train()
    total_loss = 0
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()

    scheduler.step()

    # validation
    model.eval()
    correct, total = 0, 0
    with torch.no_grad():
        for images, labels in val_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            _, preds = torch.max(outputs, 1)
            correct += (preds == labels).sum().item()
            total += labels.size(0)

    val_acc = correct / total
    print(f"Epoch {epoch+1}: Train Loss={total_loss:.4f} | Val Acc={val_acc:.6f}")

    # save best model (highest accuracy) to models directory
    if val_acc > best_val_acc:
        best_val_acc = val_acc
        torch.save(model.state_dict(), f"models/new_train/1_{MODEL_NAME}.pth")

print("EXITING TRAINING/VALIDATION LOOP...")
print("Training complete! Best validation accuracy:", best_val_acc)
