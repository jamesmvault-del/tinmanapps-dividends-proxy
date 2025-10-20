# app.py
from flask import Flask, jsonify
import json, os
from datetime import datetime

app = Flask(__name__)

DATA_PATH = "data/dividends.json"

@app.route("/")
def home():
    return jsonify({
        "status": "ok",
        "message": "TinmanApps Dividends Proxy is live!",
        "author": "TinmanApps Framework"
    })

@app.route("/dividends")
def get_dividends():
    """
    Returns dividend data if found, otherwise a fallback message.
    """
    try:
        if not os.path.exists(DATA_PATH):
            return jsonify({
                "status": "error",
                "message": "No dividends.json found on server yet",
                "timestamp": datetime.utcnow().isoformat() + "Z"
            }), 404

        with open(DATA_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)

        return jsonify({
            "status": "ok",
            "count": len(data),
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "data": data
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e),
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
