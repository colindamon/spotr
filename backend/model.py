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
Model API module for SpotR FastAPI backend

Responsibilities:
 - Load deep learning model and its weights
 - Preprocess uploaded images to match evaluation requirements
 - Run inference logic to make a prediction on car class
 - Map class ID to readable class name
"""

from backend.dataset import CAR_DATASET_INFO
from torchvision import models, transforms
from PIL import Image
import os
import torch
import torch.nn as nn


def load_model():
    model = models.resnet101(weights=None)
    model.fc = nn.Linear(model.fc.in_features, CAR_DATASET_INFO["num_classes"])
    model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'spotr_weights.pth')
    model_path = os.path.abspath(model_path) 
    state_dict = torch.load(model_path, map_location="cpu")
    model.load_state_dict(state_dict)
    model.eval()
    return model


def _preprocess_image(image: Image.Image):
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225],
        ),
    ])
    return transform(image).unsqueeze(0)


def predict(image: Image.Image, model):
    input_tensor = _preprocess_image(image)
    with torch.no_grad():
        outputs = model(input_tensor)
        predicted_class_id = outputs.argmax(dim=1).item()
        class_name = CAR_DATASET_INFO["class_names"][predicted_class_id]
    return class_name
