from flask import Flask, request, jsonify
from deepface import DeepFace
import os

app = Flask(__name__)
UPLOAD_FOLDER = "static"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
TARGET_IMAGE = os.path.join(UPLOAD_FOLDER, "reference.jpg")

@app.route("/upload", methods=["POST"])
def upload_reference():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file uploaded"}), 400
    file.save(TARGET_IMAGE)
    return jsonify({"status": "Reference image uploaded successfully."})

@app.route("/detect-frame", methods=["POST"])
def detect_frame():
    if not os.path.exists(TARGET_IMAGE):
        return jsonify({"error": "Reference image not uploaded yet."}), 400

    frame_file = request.files.get("frame")
    if not frame_file:
        return jsonify({"error": "No frame image provided."}), 400

    frame_path = os.path.join(UPLOAD_FOLDER, "frame.jpg")
    frame_file.save(frame_path)

    try:
        result = DeepFace.verify(img1_path=frame_path, img2_path=TARGET_IMAGE, enforce_detection=False)
        return jsonify({
            "verified": result["verified"],
            "distance": result["distance"],
            "threshold": result["threshold"]
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/reset", methods=["GET"])
def reset():
    if os.path.exists(TARGET_IMAGE):
        os.remove(TARGET_IMAGE)
    return jsonify({"status": "Reference image cleared."})

if __name__ == "__main__":
    app.run(debug=True)
