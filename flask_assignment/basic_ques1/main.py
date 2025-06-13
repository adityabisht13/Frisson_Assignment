from flask import Flask

app = Flask(__name__)

@app.route('/')
def Home():
    return '<h1>Hello World</h1>'


if __name__ == "__main__":
    app.run(host='localhost', port=5000)