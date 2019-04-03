from flask import Flask

app= Flask(__name__)

@app.route('/')
def home():
    return "Hi there! this is my first flask project."

if __name__ == '__main__':
    app.run(debug=True)