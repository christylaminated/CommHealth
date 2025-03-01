from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def index():
    print("✅ Flask is serving index.html")  # Debug log
    return render_template("index.html")

@socketio.on("message")
def handle_message(msg):
    print(f"📩 Message received: {msg}")
    socketio.emit("message", msg)


if __name__ == "__main__":
    print("🚀 Starting Flask WebSocket server...")  # Debug log
    socketio.run(app, debug=True, host="127.0.0.1", port=5000)
