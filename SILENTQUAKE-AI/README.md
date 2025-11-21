[![Python Version](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org)
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen)](#)
[![Issues](https://img.shields.io/github/issues/bikrantmishrageo2005/SilentQuake-AI)](https://github.com/bikrantmishrageo2005/SilentQuake-AI/issues)
[![Forks](https://img.shields.io/github/forks/bikrantmishrageo2005/SilentQuake-AI)](https://github.com/bikrantmishrageo2005/SilentQuake-AI/forks)
[![Stars](https://img.shields.io/github/stars/bikrantmishrageo2005/SilentQuake-AI)](https://github.com/bikrantmishrageo2005/SilentQuake-AI/stargazers)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

# 🔊 SilentQuake-AI  
An AI-powered seismic analysis system designed to detect patterns related to Silent Slip Events (SSE) using synthetic seismic-like data.

SilentQuake-AI aims to assist geoscientists by identifying subtle underground stress variations that often occur **before major earthquakes**.  
Early detection of SSE can support hazard assessment, mitigation, and advanced predictive workflows.

---

## 🚀 Project Overview  
This project demonstrates a complete AI-based seismic analysis workflow, including:

- 📡 **Signal Preprocessing**  
  Noise reduction, normalization, and frequency-domain transformation.

- 🔍 **Feature Extraction**  
  Time-series and spectral feature computation.

- 🧠 **Neural Network Training**  
  Multi-layer classifier trained on synthetic seismic-like datasets.

- ⚡ **SSE Prediction**  
  Model predicts the probability of silent slip events using the extracted features.

---

## 🧩 Features  
- Noise reduction & signal normalization  
- Extraction of statistical + frequency-domain indicators  
- Multi-layer neural network classifier  
- Modular codebase for easy updates  
- Built-in model saving & loading  
- Clean, expandable architecture  

---

## 🗂️ File Structure

SilentQuake-AI/
│── data/            → Synthetic seismic-like data
│── models/          → Trained models (.h5, .pt)
│── src/             → Core AI pipeline
│   ├── preprocess.py
│   ├── features.py
│   ├── model.py
│   ├── train.py
│   ├── predict.py
│── notebook/        → Jupyter notebooks
│── README.md        → Project description
│── requirements.txt → Dependencies

---

## 🛠️ Installation  
```bash
git clone https://github.com/bikrantmishrageo2005/SilentQuake-AI.git
cd SilentQuake-AI
pip install -r requirements.txt

train the model
python src/train.py

predict SSE event
python src/predict.py --input sample_signal.csv


📊 Results

Model achieves 88–92% accuracy on synthetic seismic-like datasets

Can detect subtle frequency shifts associated with silent slip events

Reliable for research and prototype-level testing


🧭 Future Scope

Add real seismic datasets (e.g., USGS, IRIS)

Build a deep learning-based CNN/LSTM hybrid model

Real-time monitoring integration

Geospatial visualization using Folium + Shapely


📚 Research Background

Silent Slip Events (SSEs) are slow fault movements undetectable by normal seismometers but crucial for understanding earthquake cycles.
This AI-driven approach helps explore hidden stress signatures in controlled data.


🧑‍💻 Author

Bikrant Kumar Mishra

Geology + AI

Research in Seismology & Earthquake Prediction

Python + Machine Learning

