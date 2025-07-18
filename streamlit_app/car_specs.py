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
Responsible for all car API call functionality, including
parsing inputs/outputs, getting API keys, and sending queries
"""

import os
import requests
from dotenv import load_dotenv


load_dotenv()

def get_api_key():
    return os.getenv("API_NINJAS_KEY")


def _parse_class_name(pred_class):
    """
    Accepts raw predicted class name
        (e.g. "BMW M5 Sedan 2010")
    Returns: tuple as (year, make, model)
        (e.g. make="BMW", model="M5", etc.)
    """
    tokens = pred_class.strip().split()
    if len(tokens) < 3:
        return (None, None, None)

    make = tokens[0]
    year = int(tokens[-1])
    if len(tokens) > 3:
        model = " ".join(tokens[1:-2])
    else:
        model = tokens[1]
    return (year, make, model)


def _parse_api_output(raw_out):
    """
    Accepts raw JSON output from API
        (e.g. "cylinders": 4, "displacement": 2.2, etc.)
    Returns: cleaned data in a dictionary
        (e.g. "engine": "2.2-liter 4-cylinder")
    """
    cleaned = []
    for entry in raw_out:
        engine = f'{entry["displacement"]}-liter {entry["cylinders"]}-cylinder'
        transmission = "Manual"
        if entry.get("transmission") == "a":
            transmission = "Automatic"
        specs = {
            "class": entry.get("class"),
            "engine": engine,
            "fuel_type": entry.get("fuel_type"),
            "transmission": transmission,
            "drivetrain": entry.get("drive"),
        }
    return specs


def fetch_car_specs(pred_class):
    """
    Fetches car specs from the API Ninjas Cars API.
    Returns: list of dicts, or None on error.
    """
    year, make, model = _parse_class_name(pred_class)
    api_key = get_api_key()
    if not api_key:
        return None

    url = "https://api.api-ninjas.com/v1/cars"
    params = {"year": year,
              "make": make,
              "model": model}
    headers = {"X-Api-Key": api_key}
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list) and data:
                return _parse_api_output(data)
        return None
    except Exception:
        return None
