import requests
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# OpenWeatherMap API Key (Replace with your actual API key)
API_KEY = "aab3c901fb7d6d2e7fcfaba881a3aa45"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route("/", methods=["GET"])
def home():
    return jsonify({"student_number": "200622929"})  # Replace with your student number

@app.route("/webhook", methods=["POST"])
def webhook():
    req = request.get_json(silent=True, force=True)
    intent_name = req.get("queryResult", {}).get("intent", {}).get("displayName")

    if intent_name == "get weather":
        city = "Barrie"  # Replace with user input if needed
        weather_data = get_weather(city)
        fulfillment_text = f"The weather in {city} is {weather_data}."
    else:
        fulfillment_text = "I couldn't find what you're looking for."

    return jsonify({"fulfillmentText": fulfillment_text})

def get_weather(city):
    """Fetch weather data from OpenWeatherMap API."""
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        description = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        return f"{description} with a temperature of {temp}°C"
    else:
        return "unavailable at the moment."



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Get the port assigned by Render
    app.run(debug=True, host="0.0.0.0", port=port)


