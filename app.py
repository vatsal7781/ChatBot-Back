from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
# client = 
openai.api_key ='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'

messages = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']

    if user_input == "quit()":
        return jsonify({'message': 'Chat ended.'})

    messages.append({"role": "user", "content": user_input})

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})

    return jsonify({'message': reply})

if __name__ == '__main__':
    app.run(debug=True)