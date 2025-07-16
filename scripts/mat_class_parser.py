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
Parses MAT meta file from dataset to CSV format

Used to create cars_meta.csv
(made from original dataset's meta MAT file)
"""

from scipy.io import loadmat
import pandas as pd

meta_mat = loadmat('dataset/car_devkit/devkit/cars_meta.mat')

records = []
for i, name in enumerate(meta_mat['class_names'][0]):
    class_id = i  # class_id is 0-indexed
    class_name = str(name[0])
    records.append({
        'class_id': class_id,
        'class_name': class_name,
    })

df = pd.DataFrame(records)
df.to_csv('dataset/cars_meta.csv', index=False)
