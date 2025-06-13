from flask import Flask,render_template,request
 

app = Flask(__name__)

@app.route('/',methods=['GET'])
def Home():
    return render_template('home.html')

@app.route('/user',methods=['POST'])
def user():
    user =request.form['user']
    return f'<h1> HELLO {user}</h1>'


if __name__ == "__main__":
    app.run(host='localhost', port=5000)