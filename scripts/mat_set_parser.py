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
Parses MAT train/test set files from dataset to CSV format

Used to create cars_train_annos.csv and cars_test_annos.csv
(made from original dataset's train/test MAT files)
"""

from scipy.io import loadmat
import pandas as pd

annos_mat = loadmat('dataset/car_devkit/devkit/cars_test_annos_withlabels.mat')
meta_mat = loadmat('dataset/car_devkit/devkit/cars_meta.mat')

class_names = [name[0] for name in meta_mat['class_names'][0]]
annos = annos_mat['annotations'][0]

records = []
for anno in annos:
    anno = anno.item()
    class_id = int(anno[4][0][0])
    class_name = class_names[class_id - 1]  # class_id is 1-indexed
    bbox = [int(anno[0][0][0]), int(anno[1][0][0]), int(anno[2][0][0]), int(anno[3][0][0])]
    filename = str(anno[5][0])
    records.append({
        'class_id': class_id,
        'class_name': class_name,
        'bbox': bbox,
        'filename': f'cars_test/{filename}'
    })

df = pd.DataFrame(records)
df.to_csv('cars_test_annos.csv', index=False)
