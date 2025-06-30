# PRODIGY_CS_02 - Pixel Manipulation for Image Encryption 🖼️🔐

This project demonstrates simple image encryption and decryption using pixel manipulation in Python.

---

## 📌 Task Description

Develop a Python program that:
- Reads an image using PIL
- Encrypts or decrypts it by applying pixel-level operations
- Saves the output as a new image file

---

## 🔧 How it Works

- Each pixel's RGB values are modified using a secret **key**
- Encryption: Add the key to each RGB value
- Decryption: Subtract the key to retrieve original pixel values

---

## 🚀 How to Run

### 🛠️ Requirements:
- Python 3
- Pillow Library (`pip install pillow`)

### ▶️ Run Command:
```bash
python image_encryptor.py
