# 🎥 Video Captioning Using CNN + LSTM

This project implements a video captioning system using a Convolutional Neural Network (CNN) encoder and a Long Short-Term Memory (LSTM) decoder, trained on the **Microsoft Research Video Description Corpus (MSVD)** dataset. The system extracts features from video frames using **ResNet-152** and generates descriptive captions using an **LSTM-based decoder**.

---

## 📌 Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Model Architecture](#model-architecture)
- [Implementation Details](#implementation-details)
- [Results](#results)
- [Challenges](#challenges)
- [Future Work](#future-work)
- [Author](#author)

---

## 🧠 Introduction

Video captioning is the task of generating natural language descriptions for video content. It requires capturing **both spatial and temporal features**, making it significantly more complex than image captioning. This model bridges **Computer Vision (CV)** and **Natural Language Processing (NLP)** using a deep learning approach.

---

## 📂 Dataset

We use the **MSVD (Microsoft Video Description)** dataset:
- ~2,000 short YouTube video clips
- ~80,000 natural language captions (~40 captions/video)
- Typical video length: 6–10 seconds
- Standard split: 1,200 train / 100 val / 670 test

---

## 🏗️ Model Architecture

### 🔹 Encoder: ResNet-152 (Pretrained on ImageNet)
- Extracts 2048-dim visual feature vectors from each frame
- Max 16 frames per video
- Features saved for reuse

### 🔸 Decoder: LSTM-based Network
- Projects visual features to LSTM input space
- Word embedding + LSTM + Fully connected layer
- Greedy decoding for inference

---

## ⚙️ Implementation Details

- **Language**: Python
- **Framework**: PyTorch
- **Frame Extraction**: OpenCV
- **Tokenizer**: BERT tokenizer (max 30 tokens)
- **Loss**: CrossEntropy (ignore padding)
- **Optimizer**: Adam (LR: 1e-4)
- **Mixed Precision**: Enabled via GradScaler
- **Batch Size**: 32
- **Epochs**: 25+

---

## 📊 Results

- **Accuracy**: Improved from <40% to ~85% over training
- **Loss**: Dropped from ~4.0 to <1.0
- **BLEU Score**: ~0.20 on validation (typical for baseline CNN-LSTM)

> 📉 Compared to state-of-the-art:
> - LSTM-TSA: ~52.8 BLEU@4
> - Baseline LSTM: ~33.3 BLEU@4
> - Our Model: ~20 BLEU (without attention)

---

## 🧪 Sample Caption

**Input**: 5-sec clip of a man mixing rice and water  
**Generated Caption**: *"A man is mixing ingredients in a bowl"*

---

## 🚧 Challenges Faced

- Handling temporal dynamics
- Memory and compute constraints
- Low BLEU score without attention
- Solo development: stuck on training/debugging for weeks

---

## 🔮 Future Work

- Add **Temporal Attention Mechanism**
- Replace LSTM with **Transformer Encoder-Decoder**
- Integrate **Audio Features** for multimodal learning
- Use **Beam Search** decoding
- Try advanced models like **LSTM-TSA**, **VideoBERT**

---

## 👤 Author

**Aryan R B Singh**  
B.Tech, Mechanical and Industrial Engineering  
Roll No: 21117028

---

## 🏷️ Tags
`video-captioning` `deep-learning` `lstm` `cnn` `nlp` `msvd` `resnet` `pytorch` `transformer` `attention`

---

## 📌 Citation

If you use or reference this work, please consider citing it in academic or project work.



