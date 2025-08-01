from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    """Return a friendly greeting."""
    return "Welcome to my Flask app!"

@app.route("/goodbye")
def goodbye():
    """Return a goodbye message."""
    return "Goodbye! See you next time."

if __name__ == "__main__":
    # Get host and port from environment variables or use defaults
    host = os.getenv("FLASK_RUN_HOST", "0.0.0.0")
    port = int(os.getenv("FLASK_RUN_PORT", 8080))
    
    # Run the app with debug mode enabled for development
    app.run(host=host, port=port, debug=True)
