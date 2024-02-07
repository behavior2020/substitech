from flask import Flask, jsonify, request
import random

app = Flask(__name__)


@app.route('/releventsubstitutes', methods=['POST'])
def post_data():
    """accepts parameters and returns list of 10 names with similarity score"""
    data = request.json  # Assuming the client sends a JSON body

    # Process the data...

    full_names = [
        "Olivia Johnson",
        "Liam Smith",
        "Emma Williams",
        "Noah Brown",
        "Ava Jones",
        "Elijah Garcia",
        "Sophia Miller",
        "Oliver Davis",
        "Isabella Rodriguez",
        "Lucas Martinez"
    ]
    names_with_scores = [{"name": name, "score": random.uniform(0, 100)} for name in full_names]
    return jsonify({"status": "success", "names": names_with_scores}), 200


# New route

@app.route('/connected', methods=['GET'])
def connect_datascience():
    """returns connection made"""
    return "Connected to DataScience"


if __name__ == '__main__':
    # Read the model
    # model_path = 'churn_model.pkl'
    # loaded_model = joblib.load(model_path)

    # Run the app to listen on any external IP and port 8080

    app.run(host='0.0.0.0', port=8080, debug=True)
