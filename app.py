from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Game logic
def generate_number():
    """Generate a random number between 1 and 100."""
    return random.randint(1, 100)

# Flask routes
@app.route("/")
def index():
    """Serve the game interface."""
    return render_template("index.html")

@app.route("/play", methods=["POST"])
def play_game():
    """Handle the game logic and return feedback."""
    try:
        #Debug: Log the incoming request JSON payload
        print(request.json)

        #Parse the JSON request data
        data = request.json

        #Check if 'guess' and 'number' exist in the request
        if not data or "guess" not in data or "number" not in data:
            return jsonify({"error": "Invalid input. Both 'guess' and 'number' are required."}), 400

        # Parse the user's guess and actual number from the request
        user_guess = data.get("guess")
        actual_number = data.get("number")

        # Convert inputs to integers
        user_guess = int(user_guess)
        actual_number = int(actual_number)

        #Determine feedback
        if user_guess < actual_number:
            return jsonify({"result": "Too Low!"})
        elif user_guess > actual_number:
            return jsonify({"result": "Too High!"})
        else:
            return jsonify({"result": f"Correct! The number was {actual_number}"})
    except ValueError:
        return jsonify({"error": "Invalid input. Please enter numeric values for 'guess' and 'number'."}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
