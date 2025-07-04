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
data package

Exposes core data utilities for spotr.
"""

from .dataset import StanfordCarsDataset
from .preprocessing import get_train_transforms, get_val_transforms
from .loader import get_dataloader


__all__ = [
    "StanfordCarsDataset",
    "get_train_transforms",
    "get_val_transforms",
    "get_dataloader",
]
