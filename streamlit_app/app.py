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
from car_specs import get_api_key, fetch_car_specs


@st.cache_resource
def get_model():
    return load_model()
MODEL = get_model()
API_KEY = get_api_key()

# Config and title
st.set_page_config(page_title="SpotR - Car Recognition", page_icon="🚗", layout="centered")
st.title("SpotR 🚗📷")

# Body
st.markdown("**SpotR** is an AI-powered car recognition tool. Start by uploading a car image and cropping to identify the model and view enthusiast specs.")
uploaded_file = st.file_uploader("Choose a car image...", type=["jpg", "jpeg", "png"])

# Logic to clear old prediction results on new image upload
if 'last_uploaded_filename' not in st.session_state:
    st.session_state['last_uploaded_filename'] = None

current_filename = uploaded_file.name if uploaded_file else None
if (st.session_state['last_uploaded_filename'] is not None and (
    current_filename != st.session_state['last_uploaded_filename'])):
    st.session_state.pop('pred_class', None)
    st.session_state.pop('cropped_img', None)
st.session_state['last_uploaded_filename'] = current_filename

# Continue body
if uploaded_file:
    image = Image.open(uploaded_file)
    st.subheader("Crop your image")
    cropped_img = st_cropper(image, box_color='red', aspect_ratio=None)
    st.image(cropped_img, caption="Cropped Image", use_container_width=True)

    if cropped_img:
        st.session_state['cropped_img'] = cropped_img

    if st.button("Identify Car"):
        with st.spinner("Predicting..."):
            pred_class = predict(cropped_img, MODEL)
            st.session_state['pred_class'] = pred_class

    if st.session_state.get('pred_class', None):
        pred_class = st.session_state['pred_class']
        st.success(f"Predicted car model: {pred_class}")

        if API_KEY:
            if st.button("Show Car Specs"):
                with st.spinner("Fetching specs..."):
                    specs = fetch_car_specs(pred_class)
                if specs:
                    st.subheader("Car Specs:")
                    for k, v in specs.items():
                        st.write(f" • **{k.capitalize()}**: {v}")
                else:
                    st.warning("No specs were found for this model ):")
        else:
            st.info("Add an API key to enable car specs lookup. (See README for instructions)")
else:
    st.info("Upload an image of a car to get started!")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <span>Made by a passionate car enthusiast. ❤️</span>
        <a href="https://github.com/colindamon" target="_blank">
            <img src="https://img.shields.io/badge/colindamon-white?style=flat&logo=github&logoColor=white&logoSize=auto&labelColor=string&color=gray" alt="GitHub" style="height:24px;">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)