const ws = new WebSocket('ws://localhost:8000/ws')
const sendButton = document.getElementById('sendButton')
const userInput = document.getElementById('userInput')
const chatHistory = document.getElementById('chatHistory')

let botMessageDiv = null

// ws.onmessage = function (event) {
// 	const message = event.data
// 	const messageDiv = document.createElement('div')
// 	messageDiv.textContent = '- ' + message
// 	chatHistory.appendChild(messageDiv)
// }

ws.onmessage = function (event) {
	const token = event.data

	// Create new line only if starting a new message
	if (!botMessageDiv) {
		botMessageDiv = document.createElement('div')
		botMessageDiv.classList.add('bot-message')
		chatHistory.appendChild(botMessageDiv)
	}

	// Append to current message
	botMessageDiv.textContent += token

	// Optional: scroll to bottom
	chatHistory.scrollTop = chatHistory.scrollHeight
}

// Reset after each message if you want to separate replies
ws.onclose = function () {
	botMessageDiv = null
}

sendButton.onclick = function () {
	const message = userInput.value
	ws.send(message)
	userInput.value = '' // Clear input field after sending
}
