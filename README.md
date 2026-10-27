---
title: SmartVision AI
sdk: gradio
app_file: app.py
python_version: 3.11
---

# SmartVision AI
Multi-class object detection using YOLOv8 and 25 COCO classes.

**AI-Powered Object Detection and Image Recognition using YOLOv8**

SmartVision AI is a computer vision project designed to detect and recognize multiple objects in images using deep learning. It uses a YOLOv8 object detection model trained on a selected subset of 25 COCO object categories.

## 🚀 Features

- **Multi-class Object Detection:** Detects objects and draws bounding boxes around them.
- **25 Object Categories:** Includes people, vehicles, animals, furniture, food, and everyday objects.
- **Confidence Scores:** Displays confidence values for detected objects.
- **Pre-trained Model Weights:** Includes the trained YOLOv8 model (`best.pt`).
- **Interactive Demo:** Supports image-based predictions through the available application.
- **Evaluation Pipeline:** Supports model validation and object detection evaluation.

## 🧠 Technologies Used

- Python
- PyTorch
- Ultralytics YOLOv8
- Streamlit
- Gradio
- Pillow
- COCO dataset annotations

## 📦 Project Structure

```text
smartvision-ai/
├── app.py
├── gradio_app.py
├── best.pt
├── requirements.txt
├── requirements_gradio.txt
├── smartvision.yaml
├── Dockerfile
└── README.md
```

## ⚙️ Installation

**1. Clone the repository**

```bash
git clone https://github.com/samyukthaa05/smartvision-ai.git
cd smartvision-ai
```

**2. Create a virtual environment (recommended)**

```bash
python -m venv venv
```

Activate it:

- Windows: `venv\Scripts\activate`
- macOS/Linux: `source venv/bin/activate`

**3. Install dependencies**

For the Streamlit application:

```bash
pip install -r requirements.txt
```

For the Gradio application:

```bash
pip install -r requirements_gradio.txt
```

## ▶️ Usage

**Run the Streamlit application**

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal, upload an image, and follow the interface to run object detection.

**Run the Gradio application**

```bash
python gradio_app.py
```

Open the local URL displayed in the terminal and use the interface to test image predictions.

> Make sure `best.pt` is in the project directory. Application commands and features depend on the current implementation of each app.

## 📊 Model Performance

The initial YOLOv8n baseline was trained for 5 epochs using CPU execution, with an image size of 416 pixels and a batch size of 4.

| Metric | Baseline result |
|---|---:|
| Precision | 0.540 |
| Recall | 0.335 |
| mAP@50 | 0.363 |
| mAP@50–95 | 0.206 |

**Evaluation details**

- Validation images: 267
- Validation object instances: 847
- Model: YOLOv8n
- Training duration: Approximately 0.693 hours

These are preliminary validation results, not final test-set results. Performance may improve with additional training, hyperparameter tuning, and further dataset validation.

## 📂 Dataset

The project uses a selected subset of COCO images and annotations covering 25 target object categories. The dataset was organized into training, validation, and test splits for object detection.

Dataset access and licensing should follow the original dataset provider's terms.

## 🔮 Future Improvements

- Train and compare additional CNN architectures for image classification.
- Improve detection performance through additional training and hyperparameter tuning.
- Evaluate the final model on a held-out test set.
- Add detailed per-class evaluation metrics and confusion-matrix visualizations.
- Improve application usability and deployment.

## 👩‍💻 Repository

GitHub: https://github.com/samyukthaa05/smartvision-ai

---

*SmartVision AI — Exploring computer vision through deep learning.*
