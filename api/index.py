from flask import Flask, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes and origins

@app.route("/quote", methods=["GET"])
def get_quote():
    try:
        response = requests.get('https://stoic-quotes.com/', headers={
            "User-Agent": "Mozilla/5.0"
        }, timeout=10)

        soup = BeautifulSoup(response.text, 'html.parser')
        quote_div = soup.find('div', class_='css-1nyywr7')

        if quote_div:
            return jsonify({
                "quote": quote_div.text.strip()
            })

        return jsonify({"error": "Quote not found."}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Root route for health check
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Stoic Quotes API is running"}), 200
