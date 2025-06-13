from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def Home():
    return f'HOME PAGE FOR DYNAMIC DATA (TYPE user name after /)'

@app.route('/<username>')
def nextpage(username):
    return f'<h1>HELLO {username}</h1>'



if __name__ == "__main__":
    app.run(host='localhost', port=5000)