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
Main FastAPI application for SpotR backend.

Responsibilities:
- Serve API endpoints for image prediction and car specs queries
- Route requests to appropriate modules for processing
- Provide a scalable inference and data API for the SpotR frontend

This is the entry point for the SpotR backend service.
"""

from fastapi import FastAPI, File, UploadFile, Query
from fastapi.middleware.cors import CORSMiddleware
from backend.model import load_model, predict
from backend.car_specs import fetch_car_specs
from PIL import Image
import io


app = FastAPI()
MODEL = load_model()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/predict")
async def predict_route(file: UploadFile):
    try:
        if not file.content_type.startswith('image/'):
            raise HTTPException(status_code=400, detail="File must be an image")
        
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes))
        pred_class = predict(image, MODEL)
        return {"pred_class": pred_class}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")


@app.get("/car-specs")
def car_specs_route(pred_class: str):
    try:
        specs = fetch_car_specs(pred_class)
        if specs is None:
            return {"error": "Specs not found or API error."}
        return specs
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Specs fetch failed: {str(e)}")


@app.get("/health")
def health_check():
    """Health check endpoint for Docker health checks"""
    return {"status": "healthy", "model_loaded": MODEL is not None}
