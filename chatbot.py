from flask import Flask, render_template, request, jsonify
import google.generativeai as ai

app = Flask(__name__)

API_KEY = 'YOUR_GEMINI_API_KEY'
ai.configure(api_key=API_KEY)

model = ai.GenerativeModel(model_name="gemini-1.5-flash")
chat = model.start_chat()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat_response():
    user_message = request.json.get('message')
    if user_message:
        response = chat.send_message(user_message)
        return jsonify({'response': response.text})
    return jsonify({'response': 'No message received.'})

if __name__ == '__main__':
    app.run(debug=True)
