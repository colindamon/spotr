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

## 🛠️ Tech Stack

| Component       | Technology        |
|-----------------|-------------------|
| Language        | Python 3.x        |
| Frontend / UI   | Streamlit         |
| ML Framework    | PyTorch           |
| Image Handling  | TorchVision       |
| Environment     | Streamlit Cloud (for MVP) |

---

## 🚧 Project Status

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
- [ ] Return car specs from prediction output

**Phase 4: Backend + Deployment**
- [ ] Migrate logic to FastAPI
- [ ] Containerize with Docker
- [ ] Optimize for performance and scale

---

## 📂 Directory Structure (Current)

```bash
spotr/
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── data
│   ├── __init__.py
│   ├── dataset.py
│   ├── loader.py
│   └── transforms.py
├── dataset
│   ├── (local Stanford Cars dataset)
│   ├── train0
│   ├── train1
│   |   ├── train1.csv
│   |   ├── val1.csv
│   |   └── test1.csv
│   ├── cars_meta.csv
│   ├── cars_train_annos.csv
│   └── cars_test_annos.csv
├── models
│   ├── train0
│   ├── train1
│   ├── spotr_weights.pth (local model weights)
│   └── model-notes.md
├── streamlit_app
│   ├── app.py
│   ├── dataset.py
│   └── model.py
├── scripts
│   ├── mat_class_parser.py
│   ├── mat_set_parser.py
│   ├── split_trainval.py
│   ├── split_trainvaltest.py
│   ├── test_cuda.py
│   └── test_dataloader.py
├── train.py
└── eval.py
```

---

## 🤝 Contributing

This project is still in early development, but contributors and testers are always welcome! Once the MVP is stable, I'll open issues for community feedback, model improvements, and dataset expansion.

---

## 📄 License

This project is licensed under the [GNU General Public License v3.0](./LICENSE). Anyone is free to use, modify, and distribute this software - as long as any derivative work is also open source under the same license.

---

## 🙋 About Me

I'm a first year computer science student and a lifelong car enthusiast. I created SpotR to combine my love of coding and cars into a fun but challenging open-source project.

Please let me know what you think. I'm always open to feedback!
