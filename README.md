# 🪄 Invisibility Cloak — Real-Time Computer Vision

## ✨ What is this?

Ever wondered what it would look like to wear an invisibility cloak?

This project recreates that effect using **real-time computer vision**.

The program first captures the background, then detects the **blue color** of the cloak using HSV color segmentation. It creates a mask around the cloak and replaces that region with the previously captured background.

The result is a simple Harry Potter-style invisibility effect — created using Python and OpenCV.

**No green screen. No Photoshop. Just computer vision.**

<br>

## 🎥 How It Works

The project follows this simple pipeline:

```text
Webcam
   ↓
Capture Background
   ↓
Capture Live Frame
   ↓
Convert BGR → HSV
   ↓
Detect Blue Color
   ↓
Create Mask
   ↓
Clean Mask
   ↓
Invert Mask
   ↓
Replace Blue Area
   ↓
Combine Background + Live Frame
   ↓
✨ Invisibility Effect
