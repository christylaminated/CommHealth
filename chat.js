// Connect to your WebSocket server
const socket = new WebSocket("wss://545cdbe7-9ae0-47f0-88b4-581f9fa61b47-00-15dsysnkuh3xx.picard.replit.dev");

socket.onopen = () => {
    console.log("✅ Connected to WebSocket server!");
};

socket.onmessage = (event) => {
    console.log("📩 Message from server:", event.data);
    const chatbox = document.getElementById("chatbox");
    let messageElement = document.createElement("p");
    messageElement.textContent = event.data;
    chatbox.appendChild(messageElement);
};

function sendMessage() {
    const messageInput = document.getElementById("messageInput");
    if (!messageInput.value) return;

    socket.send(messageInput.value); // Send message to WebSocket server
    messageInput.value = "";
}
