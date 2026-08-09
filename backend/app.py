
from flask import Flask, request, jsonify

# Create Flask application
app = Flask(__name__)

# Create multiplication API endpoint
@app.route("/multiply", methods=["POST"])
def multiply():

    # Get input data from the request
    data = request.get_json()

    # Read the two numbers
    number1 = data["number1"]
    number2 = data["number2"]

    # Perform multiplication
    result = number1 * number2

    # Return the result
    return jsonify({
        "result": result
    })


# Run the Flask application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
