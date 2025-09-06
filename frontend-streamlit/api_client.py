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
API client functions for SpotR frontend.

Responsibilities:
- Communicate with FastAPI backend to get predictions and car specs
- Serialize and send requests, handle errors, and parse responses
"""

from PIL import Image
import requests
import os
import io


BACKEND_URL = os.getenv("BACKEND_URL")


def fetch_prediction(image: Image):
    """
    Sends cropped car image to the FastAPI backend for prediction
    Returns:
        str: Predicted car class/model string, or None on error
    """
    buf = io.BytesIO()
    image.save(buf, format='JPEG')
    buf.seek(0)
    files = {'file': ('car.jpg', buf, 'image/jpeg')}
    try:
        response = requests.post(
            f"{BACKEND_URL}/predict",
            files=files,
            timeout=10
        )
        response.raise_for_status()
        return response.json().get("pred_class")
    except Exception:
        return None


def fetch_specs(pred_class: str):
    """
    Requests car specs from the FastAPI backend with class name
    Returns:
        dict: Car specs dictionary, or None on error
    """
    try:
        response = requests.get(
            f"{BACKEND_URL}/car-specs", 
            params={"pred_class": pred_class}, 
            timeout=10
        )
        response.raise_for_status()
        specs = response.json()
        if specs and "error" not in specs:
            return specs
        else:
            return None
    except Exception:
        return None
