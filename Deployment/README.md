---
title: YOLO Object Detection
emoji: 🎯
colorFrom: blue
colorTo: green
sdk: streamlit
sdk_version: 1.32.0
app_file: app.py
pinned: false
license: mit
---

# YOLO Object Detection 🎯

Real-time object detection using YOLOv8 model with Streamlit interface.

## Features

- 📸 **Image Upload & Detection**: Upload images and get instant object detection results
- 🎚️ **Adjustable Parameters**: Fine-tune confidence and IOU thresholds
- 📊 **Detailed Statistics**: Comprehensive detection statistics with charts
- 📥 **Download Results**: Download annotated images
- 🎨 **Visual Results**: Clear bounding boxes and labels on detected objects

## How to Use

1. **Upload an image** using the file uploader
2. **Adjust settings** in the sidebar:
   - Confidence threshold (default: 0.5)
   - IOU threshold (default: 0.45)
3. **View results** with:
   - Original vs Detected image comparison
   - Detection statistics and metrics
   - Class distribution chart
   - Detailed detection table
4. **Download** the annotated image

## Parameters

### Confidence Threshold
- **Range**: 0.1 - 0.95
- **Default**: 0.5
- **Lower values**: More detections, may include false positives
- **Higher values**: Fewer detections, more accurate

### IOU Threshold
- **Range**: 0.1 - 0.95
- **Default**: 0.45
- **Purpose**: Controls Non-Maximum Suppression (NMS)

## Supported Image Formats

- JPG/JPEG
- PNG
- BMP

## Technical Details

Built with:
- [Streamlit](https://streamlit.io/)
- [Ultralytics YOLO](https://github.com/ultralytics/ultralytics)
- [OpenCV](https://opencv.org/)
- [PyTorch](https://pytorch.org/)

## License

MIT License
