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
Custom PyTorch Dataset for Stanford Cars
"""

import os
import ast
import pandas as pd
from PIL import Image
from torch.utils.data import Dataset


class StanfordCarsDataset(Dataset):
    def __init__(self, csv_path, images_dir, transform=None, crop_car=True):
        """
        Args:
            csv_path (str): Path to annotation CSV.
            images_dir (str): Directory with all images.
            transform (callable, optional): Optional transform to be applied.
            crop_car (bool): Whether to crop bounding box or not.
        """
        self.car_frame = pd.read_csv(csv_path)
        self.images_dir = images_dir
        self.transform = transform
        self.crop_car = crop_car

    def __len__(self):
        return len(self.car_frame)

    def __getitem__(self, idx):
        row = self.car_frame.iloc[idx]
        img_path = os.path.join(self.images_dir, row["filename"])

        with Image.open(img_path) as img:
            img = img.convert("RGB")

            if self.crop_car:
                bbox = ast.literal_eval(row["bbox"])
                xmin, ymin, xmax, ymax = bbox
                img = img.crop((xmin, ymin, xmax, ymax))

            if self.transform:
                img = self.transform(img)

            label = int(row["label"]) - 1
            return img, label
