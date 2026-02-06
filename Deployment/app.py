import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO
import tempfile
import os
import pandas as pd
from collections import Counter

# ================= CONFIG =================
st.set_page_config(
    page_title="Emotion Detection App",
    layout="wide"
)

EMOTIONS = [
    "angry",
    "happy",
    "relax",
    "rock",
    "romantic",
    "sad",
    "surprise"
]

TARGET_WIDTH = 640     # <<< RESIZE (speed up)
FRAME_SKIP = 4         # <<< SKIP FRAME (speed up)

@st.cache_resource
def load_model():
    return YOLO("best.pt")

model = load_model()

# ================= SIDEBAR =================
st.sidebar.title("Emotion Detection App")

menu = st.sidebar.radio(
    "Choose the app mode",
    ["Home", "Image Inference", "Video Inference", "Camera Inference"]
)

st.sidebar.markdown("---")
confidence = st.sidebar.slider(
    "Confidence",
    0.1, 0.95, 0.25, 0.05
)

# ================= HOME =================
if menu == "Home":
    st.title("Emotion Detection")

    st.write(
        "This application utilizes an object detection model to detect and "
        "classify human emotions from images and videos using YOLOv8."
    )

    st.subheader("How to Use")
    st.markdown(
        """
        - Infer from image  
        - Infer from video  
        - Live camera feed  

        Use the sidebar to select a mode.
        """
    )

# ================= IMAGE =================
elif menu == "Image Inference":
    st.title("🖼️ Image Emotion Detection")
    st.caption("Emotions: angry • happy • relax • rock • romantic • sad • surprise")

    uploaded_file = st.file_uploader(
        "Upload image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:
        file_bytes = np.frombuffer(uploaded_file.read(), np.uint8)
        image_bgr = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        results = model(image_bgr, conf=confidence, verbose=False)
        result = results[0]

        st.image(
            cv2.cvtColor(result.plot(), cv2.COLOR_BGR2RGB),
            use_column_width=True
        )

        st.write("Detections:", len(result.boxes))

# ================= VIDEO =================
elif menu == "Video Inference":
    st.title("🎥 Video Emotion Detection")
    st.caption("Optimized for Hugging Face CPU")

    uploaded_video = st.file_uploader(
        "Upload video",
        type=["mp4", "avi", "mov"]
    )

    if uploaded_video:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_video.read())

        cap = cv2.VideoCapture(tfile.name)

        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)

        output_path = "output.mp4"
        out = cv2.VideoWriter(
            output_path,
            cv2.VideoWriter_fourcc(*"mp4v"),
            fps,
            (TARGET_WIDTH, int(height * TARGET_WIDTH / width))
        )

        emotion_counter = Counter()
        total_detections = 0
        frame_id = 0

        progress = st.progress(0)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame_id += 1

            # === SKIP FRAME ===
            if frame_id % FRAME_SKIP != 0:
                continue

            # === RESIZE FRAME ===
            h, w, _ = frame.shape
            scale = TARGET_WIDTH / w
            frame = cv2.resize(frame, (TARGET_WIDTH, int(h * scale)))

            results = model(frame, conf=confidence, verbose=False)
            result = results[0]

            boxes = result.boxes
            if boxes is not None:
                total_detections += len(boxes)
                for b in boxes:
                    emotion_counter[EMOTIONS[int(b.cls[0])]] += 1

            out.write(result.plot())
            progress.progress(min(frame_id / total_frames, 1.0))

        cap.release()
        out.release()

        st.success("✅ Video processing finished (optimized)")
        st.video(output_path)

        st.subheader("📊 Detection Summary")
        st.write("Total detections:", total_detections)
        st.dataframe(
            pd.DataFrame(emotion_counter.items(),
                         columns=["Emotion", "Count"]),
            use_container_width=True
        )

# ================= CAMERA =================
else:
    st.warning("Camera inference not supported on Hugging Face Spaces")
