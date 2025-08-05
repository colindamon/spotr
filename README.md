# SpotR 🚗📷

**SpotR** (read "spotter") is an AI-powered car recognition tool that identifies a vehicle’s model, year range, and enthusiast-focused specifications from an uploaded image.

---

## 🔍 Overview

SpotR is a computer vision tool that utilizes deep learning to:

- Identify the make, model, and trim of a car
- Approximate its model year range based on visual cues
- Return enthusiast-relevant data, such as horsepower, torque, MSRP, and drivetrain

The tool is built for car enthusiasts, developers, and AI hobbyists who want to explore how machine learning can be applied to automotive image recognition.

---

## 🛠️ Current Tech Stack

| Component       | Technology      |
|-----------------|-----------------|
| Language        | Python 3.x      |
| Frontend / UI   | Streamlit       |
| ML Framework    | PyTorch         |
| Image Handling  | TorchVision     |
| Environment     | Local           |

---

## 🚧 Project Status

**MVP is complete and working!**

**Phase 1: Planning and Scaffolding**
- [X] Initialize repo and structure
- [X] Define tech stack and goals
- [X] Set up local dev + Git
- [X] Add base files and licensing
- [X] Write initial `README.md`

**Phase 2: Model Prototyping**
- [X] Select dataset
- [X] Build and train baseline model
- [x] Evaluate car make/trim/year detection

**Phase 3: Interface + Inference**
- [X] Build image upload UI in Streamlit
- [X] Connect model predictions
- [X] Return car specs from prediction output

**Phase 4: Backend + Deployment**
- [ ] Migrate logic to FastAPI
- [ ] Containerize with Docker
- [ ] Optimize for performance and scale

---

## 🚀 MVP Usage Guide

### 1. **Clone the Repository**

```bash
git clone https://github.com/colindamon/spotr.git
cd spotr
```

### 2. **Install Dependencies**

SpotR requires Python 3.x. Install requirements with:

```bash
pip install -r requirements.txt
```

### 3. **Download Model Weights**

Model weights are published on [Hugging Face Hub](https://huggingface.co/colindamon/spotr_model):

Can be downloaded using this link: [Download spotr_weights.pth](https://huggingface.co/colindamon/spotr_model/resolve/main/spotr_weights.pth)

Save this file to `spotr/models/spotr_weights.pth`.


### 4. **(Optional) NinjaAPI Key for Car Specs**

SpotR enriches predictions with enthusiast car specs using [NinjaAPI](https://ninjaapi.com/).

To enable car specs lookup:
1. Sign up at [NinjaAPI](https://ninjaapi.com/) for a free API key.
2. Add your API key to the environment by creating an `.env` file with these contents:

```
NINJA_API_KEY=[your_api_key_here]
```

If no API key is set, SpotR will still identify the car but won't fetch specs.

### 5. **Run the Streamlit App**

```bash
streamlit run streamlit_app/app.py
```

Follow on-screen instructions:
1. Upload a car image (JPG, PNG)
2. Crop the image for best results
3. Click "Identify Car" to get the model prediction
4. (Optional) Click "Show Car Specs" to fetch data from NinjaAPI
5. Clear image and repeat!

---

## 🧑‍🔬 Training Your Own Model

To train your own car recognition model and recreate SpotR’s weights:

1. If you aren't using Stanford Cars for your model, prepare your dataset (see `data/` and `dataset/train1/` for formatting examples).
2. Review `train.py` for training instructions and options, then run this script.
3. Review `eval.py` for evaluation instructions and options.

---

## 📦 Files & Directories

### **Key Files**

- `models/spotr_weights.pth` - The main model weights file (on Hugging Face)
- `streamlit_app/app.py` - The main Streamlit MVP application
- `train.py` - Model training script
- `eval.py` - Model evaluation script
- `requirements.txt` - Python dependencies

### **Where to Download Files**

- **All code/scripts:** [GitHub repo](https://github.com/colindamon/spotr)
- **Model weights:** [Hugging Face Hub](https://huggingface.co/colindamon/spotr_model)

---

## 📂 Project Directory Structure

```bash
spotr/
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── data/
├── dataset/
│   └── (local Stanford Cars dataset)
├── models/
│   ├── spotr_weights.pth
│   └── model-notes.md
├── streamlit_app/
│   ├── app.py
│   ├── car_specs.py
│   ├── dataset.py
│   └── model.py
├── scripts/
├── train.py
└── eval.py
```

---

## 🤝 Contributing

Contributions, feedback, and suggestions are always welcome!  
Open an issue or pull request on [GitHub](https://github.com/colindamon/spotr).

---

## 📄 License

This project is licensed under the [GNU General Public License v3.0](./LICENSE). Anyone is free to use, modify, and distribute this software - as long as any derivative work is also open source under the same license.

---

## 🙋 About Me

I'm a first year computer science student and a lifelong car enthusiast. I created SpotR to combine my love of coding and cars into a fun but challenging open-source project.

Feel free to reach out or leave feedback!
