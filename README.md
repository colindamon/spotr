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
| Frontend        | React           |
| Backend         | FastAPI         |
| ML Framework    | PyTorch         |
| Image Handling  | TorchVision     |
| Containerization| Docker          |

---

## 🚧 Project Limitations

While SpotR is now complete and functional, there are some limitations that were encountered during development:

1. **Car Diversity Detection**: The project was envisioned to recognize a wide range of vehicles, new and old, including many of today's popular supercars. Unfortunately, during research, no open dataset contained a wide range of model years or a sufficent number of supercars. As a result, SpotR, based on the Stanford Cars dataset, struggles to identify vehicles made outside of the year range 1991 to 2012 and is limited to a select few supercars found in the dataset, such as the Bugatti Veryron, Ferrari 458, and McLaren MP4-12C.

2. **Car Spec Lookup**: SpotR uses API Ninjas' CarAPI to provide enthusiast-oriented car specifications. However, the API lacks detailed data such as exact engine formats (e.g., V8, inline-6, flat-6) or horsepower/torque figures for some vehicles. Additionally, the API does not have information for many of the cars found in the Stanford Cars dataset. This may result in the error message: "No specs were found, or the API key is missing/invalid (See README!)". While other APIs offer this data, they were paid services and were outside the scope and budget of this project.

These limitations reflect the challenges of working with open datasets and APIs while maintaining the project’s free and open-source nature. Should this project gain more attention, future iterations could explore creating a custom supercar dataset and integrationg more comprehensive APIs to deliver even richer, more accurate automotive insights.

---

## ✅ Project Status

**This project is complete and fully functional locally!**

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

**Phase 4: Backend + Local Deployment**
- [X] Migrate backend logic to FastAPI
- [X] Containerize with Docker
- [X] Optimize for performance and scale

**Phase 5: Frontend + Web Hosting**
- [X] Refactor frontend to React
- [ ] Host frontend/backend on Vercel/Render
- [ ] Deploy services and connect both

---

## 🚀 Local Deployment Guide

### 0. Prerequisites

Ensure that you have Docker Engine installed on your system. If not, follow the [Docker installation guide](https://docs.docker.com/get-docker/).

### 1. **Clone the Repository**

```bash
git clone https://github.com/colindamon/spotr.git
cd spotr
```

### 2. **Download Model Weights**

Model weights are published on [this model on Hugging Face Hub](https://huggingface.co/colindamon/spotr_model) and be downloaded using this link: [download spotr_weights.pth](https://huggingface.co/colindamon/spotr_model/resolve/main/spotr_weights.pth)

Save this file to `spotr/models/spotr_weights.pth`.

### 3. **(Optional) API Ninjas Key for Car Specs**

SpotR enriches predictions with enthusiast car specs using [API Ninjas](https://api-ninjas.com/).

To enable this feature:
1. Sign up for free at the [API Ninjas' registration page](https://api-ninjas.com/register).
2. Copy your API key found on your profile.
3. Create a `.env` file in the project root.
4. Add your API key to the `.env` file:

```
API_NINJAS_KEY=[your_api_key_here]
```

If no API key is set, SpotR will still identify the car but won't be able to fetch specs.

### 4. **Run the Application**

```bash
docker compose up --build
```

Depending on your internet speed, this command may take a few minutes on first startup as Python dependencies install and services start. 

When nearly finished, the terminal will read "Attaching to backend-1, frontend-1". Navigate to `http://127.0.0.1:5173/` start SpotR.

Follow on-screen instructions:
1. Upload a car image (JPG, PNG)
2. Crop the image for best results
3. Click "Identify Car" to get the model prediction
4. (Optional) Click "Show Car Specs" to fetch data from API Ninjas
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

- `frontend/src/App.py` - Main React frontend application
- `backend/main.py` - Main FastAPI backend application
- `models/spotr_weights.pth` - Model weights file (on Hugging Face)
- `train.py` - Model training script
- `eval.py` - Model evaluation script
- `docker-compose.yml` & `Dockerfile`'s - Docker config files
- `requirements.txt` - Main application dependencies
- `requirements-dev.txt` - Development scripts dependencies
- `archive/` - Legacy code from previous iterations of SpotR

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
├── docker-compose.yml
├── requirements.txt
├── requirements-dev.txt
├── archive/
├── backend/
│   ├── car_specs.py
│   ├── dataset.py
│   ├── main.py
│   ├── model.py
│   └── Dockerfile
├── data/
├── dataset/
├── models/
│   ├── spotr_weights.pth
│   └── model-notes.md
├── frontend/
│   ├── src/
│   │   └── App.jsx
│   └── Dockerfile
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
