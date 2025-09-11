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
Image transforms for preprocessing and augmentation
during training and validation processes.

DEFAULT: MobileNet v2
BE SURE TO CHANGE TRANSFORS FOR USE WITH OTHER MODELS
"""

from torchvision import transforms


def get_train_transforms():
    """
    Returns torchvision.transforms.Compose for training.
    Includes data augmentation and normalization.
    """
    return transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        ),
    ])


def get_val_transforms():
    """
    Returns torchvision.transforms.Compose for validation/testing.
    Only resizing and normalization.
    """
    return transforms.Compose([
        transforms.Resize(256),  # resnetxxxv2 = 232
        transforms.CenterCrop(224),  # resnetxxxv2 = 224
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225],
        ),
    ])
