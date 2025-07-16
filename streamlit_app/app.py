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
Streamlit main web interface for SpotR

NOTE: can be run with
    streamlit run app.py
"""

import streamlit as st
from streamlit_cropper import st_cropper
from PIL import Image
from model import load_model, predict


# Load model once
@st.cache_resource
def get_model():
    return load_model()
model = get_model()

# Title and body
st.set_page_config(page_title="SpotR - Car Recognition", page_icon="🚗", layout="centered")
st.title("SpotR 🚗📷")
st.markdown("**SpotR** is an AI-powered car recognition tool. Start by uploading a car image and cropping to identify the model and view enthusiast specs.")

uploaded_file = st.file_uploader("Choose a car image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.subheader("Crop your image")
    cropped_img = st_cropper(image, box_color='red', aspect_ratio=None)
    st.image(cropped_img, caption="Cropped Image", use_container_width=True)

    if st.button("Identify Car"):
        st.info("🚧 Model prediction coming soon!")
        # TODO: connect SpotR model
else:
    st.info("Upload an image of a car to get started!")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <span>Created by a car enthusiast, for car enthusiasts.</span>
        <a href="https://github.com/colindamon" target="_blank">
            <img src="https://img.shields.io/badge/GitHub-colindamon-181717?style=flat&logo=github" alt="GitHub" style="height:24px;">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)