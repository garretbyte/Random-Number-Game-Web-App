# Guess the Number Game Web App

Welcome to the **Guess the Number Game Web App**, where you can play a fun interactive game directly in your browser! The app challenges you to guess a randomly generated number between 1 and 100.

---

## Features
- Random number generation on each page load.
- User-friendly interface with feedback for each guess.
- Hints like "Too High!" or "Too Low!" to guide your next guess.
- Instant feedback on the result.

---

## Prerequisites
To run this web app, you need:
1. **Python 3.x** installed on your system.
2. **Flask** Python library. Install it using:
   ```bash
   pip install flask
   ```

---

## Installation and Setup
1. Clone or download this repository to your computer.

2. **Project Directory Structure**:
   ```
   my_web_app/
   ├── app.py               # Backend logic
   ├── random numb game.py  # Game logic (if separate)
   ├── templates/
   │   └── index.html       # Frontend interface
   ├── static/
   │   └── style.css        # Optional styling
   └── README.md            # Instructions for usage
   ```

3. Navigate to the project directory in your terminal:
   ```bash
   cd my_web_app
   ```

4. Run the Flask app:
   ```bash
   python app.py
   ```

---

## Accessing the Web App
1. Once the server is running, open your web browser.
2. Go to the following URL:
   ```
   http://localhost:8000
   ```

3. Start playing the game! 🎮

---

## Playing the Game
1. Enter your guess in the input box.
2. Click the **Submit** button.
3. Check the feedback:
   - **"Too High!"**: Your guess is greater than the number.
   - **"Too Low!"**: Your guess is less than the number.
   - **"Correct!"**: You guessed the right number.

4. Refresh the page to start a new game with a fresh random number.

---

## Testing on Other Devices
To access the app from other devices on your local network:
1. Find your computer's IP address using:
   ```bash
   ifconfig
   ```
   Look for the `inet` address under your network (e.g., `192.168.1.10`).

2. Replace `localhost` with your IP address in the URL:
   ```
   http://192.168.1.10:8000
   ```

3. Ensure your computer's firewall allows incoming connections on port 8000.

---

## License
This project is for educational purposes. Feel free to modify and expand it for your own use!

---

## Troubleshooting
1. **Flask not installed**: Run `pip install flask`.
2. **Port already in use**: Change the port in `app.py`:
   ```python
   app.run(host="0.0.0.0", port=8080)
   ```

For any other issues, feel free to open an issue or contact the project creator.
