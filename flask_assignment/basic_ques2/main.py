from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('home.html')

@app.route('/nextpage')
def nextpage():
    return '<h1>Welcome On The Next Page</h1>'


if __name__ == "__main__":
    app.run(host='localhost', port=5000)