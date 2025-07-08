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
Quick script to randomly split annotations into
training set and validation set for train.py module
"""

import pandas as pd
from sklearn.model_selection import train_test_split


INPUT_CSV = 'cars_train_annos.csv'
TRAIN_CSV = 'train0.csv'
VAL_CSV = 'val0.csv'
TRAIN_RATIO = 0.8  # 80% train, 20% val

df = pd.read_csv(INPUT_CSV)

# split into train and val sets
train_df, val_df = train_test_split(df, train_size=TRAIN_RATIO, shuffle=True, random_state=42)

# make new csv files
train_df.to_csv(TRAIN_CSV, index=False)
val_df.to_csv(VAL_CSV, index=False)

print(f"Train set: {len(train_df)} samples")
print(f"Validation set: {len(val_df)} samples")
