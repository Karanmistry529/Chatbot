from flask import Flask, request, jsonify

app = Flask(__name__)

# Route 1: Returns student number
@app.route('/')
def home():
    return jsonify({"student_number": "200611529"})

# Route 2: Webhook for Dialogflow
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)  # Parse JSON from Dialogflow
    response = {
        "fulfillmentText": "Webhook response from Flask!"
    }
    return jsonify(response)



if __name__ == '__main__':
    app.run(debug=True)
