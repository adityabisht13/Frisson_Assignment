from flask import Flask, request, render_template, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)

file_status = {}  # To store file name and URL
UPLOAD_FOLDER = 'inter_ques6/static/files'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Create folder if not exists


@app.route("/", methods=['GET'])
def root():
    return redirect('/upload')

@app.route("/upload", methods=['GET'])
def upload_page():
    return render_template('file.html')

@app.route("/remove", methods=['GET'])
def remove():
    if os.path.exists(UPLOAD_FOLDER):
        for file in os.listdir(UPLOAD_FOLDER):
            os.remove(os.path.join(UPLOAD_FOLDER, file))
    file_status.clear()
    return redirect('/upload')


@app.route("/", methods=['POST'])
def upload_file():
    files = request.files.getlist('myfile') 

    for file in files:
        if file and file.filename != "":
            filename = file.filename
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)

            file_url = url_for('static', filename=f'files/{filename}', _external=True)
            file_status[filename] = f'<a href="{file_url}" target="_blank">{file_url}</a>'

    # Create a DataFrame and return it as an HTML table
    df = pd.DataFrame(file_status.items(), columns=["Filename", "URL"])
    return f'''
        {df.to_html(render_links=True, escape=False, index=False)}
        <br><br>
        <a href="/upload">Upload More Files</a>
        <br>
        <a href='/remove'>Remove all file</a?
    '''

if __name__ == '__main__':
    app.run()
