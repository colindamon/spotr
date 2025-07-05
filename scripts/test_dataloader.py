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
test script for data loader functionality
"""

import matplotlib.pyplot as plt
import torch
from data.dataset import StanfordCarsDataset
from data.transforms import get_train_transforms, get_val_transforms
from data.loader import get_dataloader


def imshow(img, mean, std):
    """Unnormalize and show a tensor image."""
    img = img.numpy().transpose((1, 2, 0))
    img = std * img + mean
    img = img.clip(0, 1)
    plt.imshow(img)
    plt.axis('off')


if __name__ == "__main__":
    # Paths to data
    csv_path = "dataset/stanford_cars/cars_train_annos.csv"
    images_dir = "dataset/stanford_cars/cars_train"

    # Instantiate dataset and dataloader
    dataset = StanfordCarsDataset(
        csv_path=csv_path,
        images_dir=images_dir,
        transform=get_train_transforms(224)
    )
    dataloader = get_dataloader(dataset, batch_size=4, shuffle=True)

    # Load a single batch
    images, labels = next(iter(dataloader))
    print(f"Batch images shape: {images.shape}")
    print(f"Batch labels: {labels}")

    # Visualize the images (first 4)
    mean = torch.tensor([0.485, 0.456, 0.406])
    std = torch.tensor([0.229, 0.224, 0.225])
    plt.figure(figsize=(10, 4))
    for i in range(4):
        plt.subplot(1, 4, i+1)
        imshow(images[i].cpu(), mean, std)
        plt.title(f"Label: {labels[i].item()}")
    plt.tight_layout()
    plt.show()
