from flask import Flask, request, jsonify

app = Flask(__name__)

# Route to return student number
@app.route("/", methods=["GET"])
def home():
    return jsonify({"student_number": "200622929"})  # Replace with your student number

# Webhook route for Dialogflow fulfillment
@app.route("/webhook", methods=["POST"])
def webhook():
    req = request.get_json(silent=True, force=True)
    intent_name = req.get("queryResult", {}).get("intent", {}).get("displayName")

    if intent_name == "get_grocery_list":
        fulfillment_text = "Your grocery list includes milk, eggs, bread, and vegetables."
    else:
        fulfillment_text = "I couldn't find what you're looking for."

    return jsonify({"fulfillmentText": fulfillment_text})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

