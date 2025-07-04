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
Helper for creating PyTorch DataLoaders for training, validation, and testing.
"""

from torch.utils.data import DataLoader


def get_dataloader(dataset, batch_size=32, shuffle=True, num_workers=4, pin_memory=True, drop_last=False):
    """
    Returns a PyTorch DataLoader for the given dataset.

    Args:
        dataset (torch.utils.data.Dataset): The dataset to load from.
        batch_size (int): Number of samples per batch.
        shuffle (bool): Whether to shuffle the data (usually True for training, False for validation/test).
        num_workers (int): Number of subprocesses to use for data loading.
        pin_memory (bool): Whether to use pinned (page-locked) memory. Set True if using CUDA.
        drop_last (bool): Whether to drop the last incomplete batch.

    Returns:
        torch.utils.data.DataLoader: DataLoader instance.
    """
    return DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=shuffle,
        num_workers=num_workers,
        pin_memory=pin_memory,
        drop_last=drop_last
    )
