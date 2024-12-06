from flask import Flask, render_template, request
import google.generativeai as genai
API_KEY = "AIzaSyAcFmNvD4qsT8LSyJzt1mLwg9KtFkHXpq4"
# Initialize the Flask app
app = Flask(__name__)

# Configure Google Generative AI
# API_KEY = "your_api_key_here"  # Replace with your actual API key
genai.configure(api_key=API_KEY)

# Define the generative model
model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_text = request.form.get('prompt')
    try:
        response = model.generate_content(user_text)
        bot_response = response.text
    except Exception as e:
        bot_response = f"Error: {e}"
    return {"response": bot_response}

if __name__ == '__main__':
    app.run(debug=True)
