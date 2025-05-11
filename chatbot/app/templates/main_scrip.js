const ws = new WebSocket('ws://localhost:8000/ws')
const sendButton = document.getElementById('sendButton')
const userInput = document.getElementById('userInput')
const chatHistory = document.getElementById('chatHistory')

ws.onmessage = function (event) {
	const message = event.data
	const messageDiv = document.createElement('div')
	messageDiv.textContent = '- ' + message
	chatHistory.appendChild(messageDiv)
}

sendButton.onclick = function () {
	const message = userInput.value
	ws.send(message)
	userInput.value = '' // Clear input field after sending
}
