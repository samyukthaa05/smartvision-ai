
import gradio as gr
from ultralytics import YOLO
from PIL import Image

model = YOLO("best.pt")

def detect(image, confidence):
    if image is None:
        return None, "Please upload an image."

    results = model.predict(
        source=image,
        conf=confidence,
        imgsz=416,
        verbose=False
    )
    plotted = results[0].plot()
    plotted = Image.fromarray(plotted[:, :, ::-1])

    boxes = results[0].boxes
    if boxes is None or len(boxes) == 0:
        return plotted, "No objects detected."

    lines = []
    for box in boxes:
        cls_id = int(box.cls[0])
        score = float(box.conf[0])
        name = model.names[cls_id]
        lines.append(f"{name}: {score:.2%}")

    return plotted, "\n".join(lines)

demo = gr.Interface(
    fn=detect,
    inputs=[
        gr.Image(type="pil", label="Upload an image"),
        gr.Slider(0.1, 0.9, value=0.25, step=0.05,
                  label="Confidence threshold")
    ],
    outputs=[
        gr.Image(type="pil", label="Detection result"),
        gr.Textbox(label="Detected objects")
    ],
    title="SmartVision AI",
    description="Detects objects from 25 selected COCO classes."
)

if __name__ == "__main__":
    demo.launch()
