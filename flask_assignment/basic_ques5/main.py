from flask import Flask,  request, render_template,redirect

app = Flask(__name__)

@app.route('/')
def root():
    return redirect('/login')

@app.route('/login' ,methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/' , methods=['POST'])
def home():
    user=request.form['name']
    email=request.form['email']
    phone=request.form['phone']
    return f'''
           <h1>USER INFO</h1><br>
           user name  -> {user} <br>
           user email  -> {email}<br>
           user phone no  -> {phone}<br>
           <a href='/login'>LOG OUT</a>

            '''
if __name__ == '__main__':
    app.run(host='localhost',port=5000)

