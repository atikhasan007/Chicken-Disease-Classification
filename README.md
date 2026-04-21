# 🐔 Chicken Disease Classification using Deep Learning (CNN + Flask)

An end-to-end **Deep Learning Project** for classifying chicken diseases using image data from **Kaggle dataset**, built with **CNN (VGG16 Transfer Learning)** and deployed using **Flask API + Web Interface**.

---

## 🚀 Project Overview

This project is an AI-based image classification system that detects chicken diseases from images.  
It follows a complete **MLOps-style pipeline** including:

- Data ingestion (from Kaggle dataset)
- Data preprocessing & augmentation
- Transfer learning (VGG16 CNN model)
- Model training & evaluation
- Flask-based deployment
- Real-time image prediction UI

---

## 🎯 Business Objectives

- Early detection of chicken diseases using AI
- Reduce manual inspection cost in poultry farms
- Improve livestock health monitoring
- Provide fast and accurate image-based diagnosis
- Build production-ready ML pipeline

---

## 📊 Data Sources

- Dataset collected from **Kaggle**
- Image categories:
  - Healthy Chicken
  - Diseased Chicken
- Data format: Images (JPG/PNG)
- Preprocessing: resizing (224x224), normalization, augmentation

---

## 📈 Exploratory Data Analysis (EDA)

- Class distribution visualization
- Image quality inspection
- Dataset balancing check
- Augmentation techniques:
  - Rotation
  - Zoom
  - Flip
  - Rescaling

---

## 🤖 Models Used

### 🧠 CNN Architecture
- Pretrained **VGG16 (Transfer Learning)**
- Frozen convolutional base
- Custom dense classifier head:
  - Flatten layer
  - Dense layer (output: 2 classes)

### ⚙️ Why VGG16?
- Strong feature extraction capability
- Works well on small datasets
- Faster convergence using pretrained weights

---

## 📏 Evaluation Metrics

### 🧪 Final Results
- Training Accuracy: **89.53%**
- Validation Accuracy: **92.19%**
- Final Training Loss: **0.6456**
- Final Validation Loss: **0.8410**

### 📊 Performance Summary
- Best validation accuracy achieved: **92.19%**
- Model shows stable convergence after epoch 3
- Good generalization on validation data

---



### 🔹 Features
- Upload image from UI
- Base64 image decoding
- Real-time prediction response
- JSON output result

---

## 📁 Project Structure

# WorkFlow
1. Update config.yaml
2. Update params.yaml
3. Update the entity
4. Update the configuration manager in src config
5. Update the components
6. Update the pipeline
7. Update the main.py
9. Update the app.py

# how to run ?

### STEPS:


Clone this reporsitory
```bash
https://github.com/atikhasan007/Chicken-Disease-Classification.git
```

```bash
conda create -n cnncls python=3.8

```

```bash
conda activate cnncls

```

### step 02- install the requirements
```bash
pip install -r requirements.txt

```

## web app result

<img width="1049" height="790" alt="Screenshot 2026-04-21 121535" src="https://github.com/user-attachments/assets/6ba4d781-7a6a-42ad-bc80-29e92096b2a0" />

<img width="1033" height="772" alt="Screenshot 2026-04-21 121645" src="https://github.com/user-attachments/assets/198ec421-f827-4e5f-9f58-db8d9ad5f342" />



