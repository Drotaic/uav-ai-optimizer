# UAV AI Optimizer

TensorFlow model optimization pipeline for deploying AI vision models on UAVs. Converts standard models to TensorFlow Lite for fast, lightweight, real-time inference on edge devices like Raspberry Pi or NVIDIA Jetson.

## 🧠 What It Does
- Converts TensorFlow models (SavedModel or Keras) to TensorFlow Lite
- Compares size and speed
- Optionally quantizes model (float16, int8)
- Prepares for drone deployment

## 🚁 Use Case
Drones require small, fast models. This tool enables converting your AI models for crack detection, survivor detection, or segmentation into deployable TFLite versions.

## 📁 Structure
- `models/`: Original and converted models
- `scripts/`: Conversion and comparison scripts
- `notebooks/`: Visual conversion + benchmark notebook
- `assets/`: Charts or side-by-side stats

## 🔮 Future Work
- Integrate with onboard runtime (e.g., TFLite on Pi)
- Build full AI deployment pipeline for field tests
