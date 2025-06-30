# SpotR 🚗📷

**SpotR** (read as "spotter") is an AI-powered car recognition tool that identifies a vehicle’s model, year range, and enthusiast-focused specifications from an uploaded image.

---

## 🔍 Overview

SpotR is a computer vision tool that utilizes deep learning to:

- Identify the make, model, and trim of a car
- Approximate its model year range based on visual cues
- Return enthusiast-relevant data such as horsepower, torque, MSRP, and drivetrain

The tool is built for car enthusiasts, developers, and AI hobbyists who want to explore how machine learning can be applied to automotive image recognition.

---

## 🛠️ Tech Stack

| Component       | Technology        |
|-----------------|-------------------|
| Language        | Python 3.x        |
| Frontend / UI   | Streamlit         |
| ML Framework    | PyTorch           |
| Image Handling  | OpenCV            |
| Environment     | Streamlit Cloud (MVP) |

---

## 🚧 Project Status

**Phase 1: Planning and Scaffolding**
- [X] Initialize repo and structure
- [X] Define tech stack and goals
- [X] Set up local dev + Git
- [X] Add base files and licensing
- [X] Write initial `README.md`

**Phase 2: Model Prototyping**
- [ ] Select dataset
- [ ] Build and train baseline model
- [ ] Evaluate car-year/trim detection

**Phase 3: Interface + Inference**
- [ ] Build image upload UI in Streamlit
- [ ] Connect model predictions
- [ ] Return car specs from prediction output

**Phase 4: Backend + Deployment**
- [ ] Migrate logic to FastAPI
- [ ] Containerize with Docker
- [ ] Optimize for performance and scale

---

## 📂 Directory Structure (current)

spotr/
├── app.py # Streamlit interface
├── inference.py # Prediction logic
├── preprocessing.py # Image preprocessing
├── requirements.txt
├── dev-notes.md # Planning, ideas, and roadmap
├── LICENSE
└── README.md

---

## 🤝 Contributing

This project is still in early development, but contributors and testers are always welcome! Once the MVP is stable, I'll open issues for community feedback, model improvements, and dataset expansion.

---

## 📄 License

This project is licensed under the [GNU General Public License v3.0](./LICENSE).
You are free to use, modify, and distribute this software - as long as any derivative work is also open source under the same license.

---

## 🙋 About the Creator

I'm a first year computer science student and a lifelong car enthusiast. I created SpotR to combine my love of coding and cars into a fun and challenging open-source project.

Let me know what you think. I'm always open to feedback!
