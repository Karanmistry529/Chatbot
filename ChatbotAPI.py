from flask import Flask, request, jsonify

app = Flask(__name__)

# Route 1: Returns student number
@app.route('/')
def home():
    return jsonify({"student_number": "200611529"})

# Route 2: Webhook for Dialogflow
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()
    intent_name = req.get('queryResult', {}).get('intent', {}).get('displayName')

    if intent_name == "Employee Details":
        # Extract the employee name from the request
        employee_name = req.get('queryResult', {}).get('parameters', {}).get('Employee_name', 'Unknown')

        # Example response: You can replace this with data from your database
        employee_data = {
            "John": "John is a Project Manager and is currently active.",
            "Jane": "Jane is a Site Engineer and is on leave.",
        }
        response_text = employee_data.get(employee_name, f"Sorry, I couldn't find details for {employee_name}.")

        return jsonify({"fulfillmentText": response_text})

    return jsonify({"fulfillmentText": "I'm sorry, I can't handle that request."})



if __name__ == '__main__':
    app.run(debug=True)
