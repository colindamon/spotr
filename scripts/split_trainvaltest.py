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
Randomly splits train and test annotations
into three CSVs for train/val/test sets
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from pathlib import Path


# NOTE: change values/Paths as needed
#  train/val/test sizes must add to 1.0
TRAIN_SIZE = 0.70
VAL_SIZE = 0.15
TEST_SIZE = 0.15
input_csv_train = Path("dataset/train1/cars_train_annos.csv")
input_csv_test = Path("dataset/train1/cars_test_annos.csv")

csv_dir = input_csv_train.parent.resolve()
train_df = pd.read_csv(input_csv_train)
test_df = pd.read_csv(input_csv_test)

# combine dataframes
df = pd.concat([train_df, test_df], ignore_index=True)

# split for test dataframe
rest_df, test_df = train_test_split(
    df, test_size=TEST_SIZE, stratify=df['class_id'], random_state=42
)

# second split for val dataframe
val_size = VAL_SIZE / (1.0 - TEST_SIZE)
train_df, val_df = train_test_split(
    rest_df, test_size=val_size, stratify=rest_df['class_id'], random_state=42
)

# save splits
train_df.to_csv(csv_dir / "1train.csv", index=False)
val_df.to_csv(csv_dir / "1val.csv", index=False)
test_df.to_csv(csv_dir / "1test.csv", index=False)

print(f"Train set: {len(train_df)} samples")
print(f"Validation set: {len(val_df)} samples")
print(f"Test set: {len(test_df)} samples")
