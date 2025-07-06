# 🧠 VisionAI Backend – Real-Time Face Detection API with Flask + DeepFace

This is a backend-only Flask API that powers real-time face verification using DeepFace. Designed for applications like surveillance, criminal identification, or any custom AI-based face recognition system.

---

## 🚀 Features

- Upload a reference image (e.g. suspect/criminal)
- Real-time webcam frame matching
- Uses DeepFace to compare facial embeddings
- API-only: can be used with any frontend (HTML/React/Android)
- Plug & play REST endpoints

---

## 🗂️ Folder Structure

```
visionai-backend/
├── app.py
├── requirements.txt
└── static/
    ├── reference.jpg     # Uploaded target face
    └── frame.jpg         # Frame to compare with
```

---

## ⚙️ Setup Instructions (Local)

### 1. Clone the repository

```bash
git clone https://github.com/your-username/visionai-backend.git
cd visionai-backend
```

### 2. Create virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🧪 API Endpoints

### 🔹 POST `/upload`
Uploads and stores the reference image for future comparisons.

- **Body (form-data)**:
  - `file`: image file (jpg/png)

### 🔹 POST `/detect-frame`
Compares the uploaded reference image with the current webcam frame.

- **Body (form-data)**:
  - `frame`: camera frame image

- **Returns**:
```json
{
  "verified": true,
  "distance": 0.34,
  "threshold": 0.4
}
```

### 🔹 GET `/reset`
Deletes the stored reference image (useful for refreshing the session).

---

## 🧠 How it Works

- DeepFace extracts facial embeddings from both the reference and input frame.
- It then compares the two and returns whether they match within a certain threshold.

---

## 📦 Tech Stack

- Python 3
- Flask
- DeepFace
- OpenCV

---

## 💡 Use Cases

- Surveillance & criminal detection systems
- Real-time visitor verification
- AI-powered access control apps
- Smart mirror / kiosk setups

---

## ✅ Future Plans

- [ ] Multi-face matching support
- [ ] Add MongoDB-based history tracking
- [ ] Render/Railway deployment script
- [ ] Token-based authentication

---

## 👨‍💻 Author

Built by [Aryan Barde](https://www.linkedin.com/in/aryan-barde/)  
Feel free to fork, clone, and enhance!

---

## 🛡️ License

MIT License – free for personal & commercial use.
