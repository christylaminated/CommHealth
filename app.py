from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
import google.generativeai as genai
import os

import logging

logging.basicConfig(
    filename="debug.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger()

logger.debug("will socket work?")

# initialize Flask app and websockets

#initialize Flask app and websocket
app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app, cors_allowed_origins="*")
logger.debug("socket initialized!")


# setting up gemini api
logger.debug("gemini api working?")
API_KEY = "AIzaSyBv40o1t8gV7iPzdTUXobTosil7SvMS-y0"
genai.configure(api_key=API_KEY)
chatbot = genai.GenerativeModel("gemini-1.5-pro")  # very empathetic!
logger.debug("gemini created")


#setting up gemini api
logger.debug("gemini api working?")
API_KEY = "AIzaSyBv40o1t8gV7iPzdTUXobTosil7SvMS-y0"
genai.configure(api_key=API_KEY)
chatbot = genai.GenerativeModel("gemini-1.5-pro") #very empathetic!
logger.debug("gemini created")


@app.route("/")
def index():
    logger.debug("Flask is serving index.html")  # Debug log
    return render_template("index.html")


@socketio.on("message")
def handle_message(msg):
    logger.debug(f"📩 Message received: {msg}")
    socketio.emit("message", msg)

#ai chat
@app.route("/chatbot", methods=["POST"])
def chatbot_response():
    logger.debug("in chatbox function")
    data = request.json
    user_input = data.get("text", "")

    prompt = f"""
    You are a compassionate AI therapist trained to provide emotional support.
    Your responses should be gentle, supportive, and helpful.
    
    This is what the user is saying: {user_input}
    repond in a helpful way.
    """
    ai_reply = "I'm here to listen, but I didn't quite understand that."
    while True:
        try:
            response = chatbot.generate_content(prompt)
            if response and hasattr(response, "text"):
                ai_reply = response.text
                break
        except Exception as e:
            logger.debug(f"error: {e}")
    if response and hasattr(response, "text"):
        logger.debug(f"AI Response Received: {ai_reply}")
    else:
        logger.debug("failed to get a response after 5 tries")
    
    logger.debug(f"ai response: {ai_reply}")
    return jsonify({"reply": ai_reply})
    






# ai chat
@app.route("/chatbot", methods=["POST"])
def chatbot_response():
    logger.debug("in chatbox function")
    data = request.json
    user_input = data.get("text", "")

    prompt = f"""
    You are a compassionate AI therapist trained to provide emotional support.
    Your responses should be gentle, supportive, and helpful.

    This is what the user is saying: {user_input}
    repond in a helpful way.
    """
    ai_reply = "I'm here to listen, but I didn't quite understand that."
    while True:
        try:
            response = chatbot.generate_content(prompt)
            if response and hasattr(response, "text"):
                ai_reply = response.text
                break
        except Exception as e:
            logger.debug(f"error: {e}")
    if response and hasattr(response, "text"):
        logger.debug(f"AI Response Received: {ai_reply}")
    else:
        logger.debug("failed to get a response after 5 tries")

    logger.debug(f"ai response: {ai_reply}")
    return jsonify({"reply": ai_reply})


if __name__ == "__main__":
    logger.debug("Starting Flask WebSocket server...")  # Debug log
    socketio.run(app, debug=True, host="127.0.0.1", port=5000)
    logger.debug("worked")




