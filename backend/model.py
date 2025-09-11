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

import torch
import gc
import psutil
from torchvision import models, transforms
from PIL import Image
import os
import torch.nn as nn
from backend.dataset import CAR_DATASET_INFO


class LazyPyTorchModel:
    def __init__(self):
        self.model = None
        self.model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'spotr_mobilenetv2.pth')
    
    def _load_model(self):
        """Load model only when needed"""
        if self.model is None:
            torch.cuda.empty_cache() if torch.cuda.is_available() else None
            gc.collect()
            
            model = models.resnet101(weights=None)
            model.fc = nn.Linear(model.fc.in_features, CAR_DATASET_INFO["num_classes"])
            
            state_dict = torch.load(self.model_path, map_location="cpu", mmap=True)
            model.load_state_dict(state_dict)
            model.eval()

            self.model = torch.quantization.quantize_dynamic(
                model, {nn.Linear, nn.Conv2d}, dtype=torch.qint8
            )
    
    def predict(self, image: Image.Image):
        """Make prediction with memory cleanup"""
        self._load_model()
        transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225],
            ),
        ])
        input_tensor = transform(image).unsqueeze(0)

        with torch.no_grad():
            outputs = self.model(input_tensor)
            predicted_class_id = outputs.argmax(dim=1).item()
            class_name = CAR_DATASET_INFO["class_names"][predicted_class_id]
        del input_tensor, outputs
        gc.collect()
        return class_name
    
    def clear_model(self):
        """Clear model from memory"""
        if self.model is not None:
            del self.model
            self.model = None
            gc.collect()


_model_instance = None

def get_model_instance():
    global _model_instance
    if _model_instance is None:
        _model_instance = LazyPyTorchModel()
    return _model_instance
