# SpotR 🚗📷

**SpotR** (read "spotter") is an AI-powered car recognition tool that identifies a vehicle’s make, model, approximate year, and enthusiast-focused specifications from an uploaded image.

---

## 🔍 Overview

SpotR is a computer vision tool that utilizes deep learning to:

- Identify the make, model, and trim of a car
- Approximate its model year
- Return enthusiast-relevant data, such as class, engine information, drivetrain, etc.

The tool is built for car enthusiasts, developers, and AI hobbyists who want to explore how machine learning can be applied to automotive image recognition.

---

## 🛠️ Current Tech Stack

| Component       | Technology      |
|-----------------|-----------------|
| Language        | Python 3.x      |
| Frontend / UI   | Streamlit       |
| Backend         | FastAPI         |
| ML Framework    | PyTorch         |
| Image Handling  | TorchVision     |
| Containerization| Docker          |

---

## 🚧 Project Limitations

While SpotR is now complete and functional, there are some limitations that were encountered during development:

1. **Supercar Detection**: The project was envisioned to recognize a wide range of vehicles, including popular supercars. Unfortunately, during research, no open dataset containing supercars (or datasets with normal cars that included a significant number of supercars) was found. As a result, SpotR is based on the Stanford Cars dataset and struggles to identify many supercars as originally planned.

2. **Car Spec Lookup**: SpotR uses API Ninja’s CarAPI to provide enthusiast-oriented car specifications. However, the API lacks detailed data such as exact engine formats (e.g., V8, inline-6, flat-6) or horsepower/torque figures for some vehicles. While other APIs offer this data, they were paid services and were outside the scope and budget of this project.

These limitations reflect the challenges of working with open datasets and APIs while maintaining the project’s free and open-source nature. Should this project gain more attention, future iterations could explore creating a custom supercar dataset and integrationg more comprehensive APIs to deliver even richer, more accurate automotive insights.

---

## ✅ Project Status

**This project is complete and fully functional!**

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
- [X] Migrate logic to FastAPI
- [X] Containerize with Docker
- [X] Optimize for performance and scale

---

## 🚀 Usage Guide

### Prerequisites

Ensure that you have Docker installed on your system. If not, follow the [Docker installation guide](https://docs.docker.com/get-docker/).

### 1. **Clone the Repository**

```bash
git clone https://github.com/colindamon/spotr.git
cd spotr
```

### 2. **Download Model Weights**

Model weights are published on [Hugging Face Hub](https://huggingface.co/colindamon/spotr_model):

Can be downloaded using this link: [Download spotr_weights.pth](https://huggingface.co/colindamon/spotr_model/resolve/main/spotr_weights.pth)

Save this file to `spotr/models/spotr_weights.pth`.

### 3. **(Optional) NinjaAPI Key for Car Specs**

SpotR enriches predictions with enthusiast car specs using [NinjaAPI](https://ninjaapi.com/).

To enable car specs lookup:
1. Sign up at [NinjaAPI](https://ninjaapi.com/) for a free API key.
2. Add your API key to the environment by creating an `.env` file with these contents:

```
NINJA_API_KEY=[your_api_key_here]
```

If no API key is set, SpotR will still identify the car but won't fetch specs.

### 4. **Run the Application**

```bash
docker compose up --build
```

This will start the SpotR application. Navigate to `http://localhost:8000` in your browser to use it.

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

- `frontend/app.py` - Main Streamlit frontend application
- `backend/main.py` - Main FastAPI backend application
- `models/spotr_weights.pth` - Model weights file (on Hugging Face)
- `train.py` - Model training script
- `eval.py` - Model evaluation script
- `docker-compose.yml` & `Dockerfile` - Docker containerization config files

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
├── docker-compose.yml
├── Dockerfile
├── backend/
│   ├── car_specs.py
│   ├── dataset.py
│   ├── main.py
│   └── model.py
├── data/
├── dataset/
├── models/
│   ├── spotr_weights.pth
│   └── model-notes.md
├── frontend/
│   ├── api_client.py
│   └── app.py
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
