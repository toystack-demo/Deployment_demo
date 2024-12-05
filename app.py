from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! I am a demo application!!Welcome to Toystack!'

if __name__ == '__main__':
    app.run(debug=True)
