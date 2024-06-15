from flask import Flask,render_template


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "welcome to care connect"


@app.route('/login')
def login():
    return 'welcome to the login page'

@app.route('/signup')
def signup():
    return 'welcome to the signup page'

@app.route('/home')
def home():
    return 'welcome to the home page'

@app.route('/pillrem')
def pillrem():
    return 'welcome to the pill reminder page'

@app.route('/symptomtracker')
def symtra():
    return 'welcome to the symptom tracker'

@app.route('/chat')
def chat():
    return 'welcome to the chatbot page'

if __name__ == '__main__':
    app.run(debug =True)