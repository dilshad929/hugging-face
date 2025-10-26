from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
HEADERS = {"Authorization": f"Bearer {os.getenv('HF_TOKEN')}"}

@app.route("/")
def home():
    return "✅ Hugging Face API is running! Use POST /summarize with JSON {\"text\": \"your text here\"}"

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json()
    text = data.get("text", "")
    response = requests.post(API_URL, headers=HEADERS, json={"inputs": text})
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
