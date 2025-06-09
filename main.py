from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__)

@app.route('/' , methods=['GET'])
def Home():
    return render_template("index.html")

@app.route('/scraper', methods=['POST'])
def scraper():
    query =request.form['query']
    save_img='static/images'


    if os.path.exists(save_img):
        for file in os.listdir(save_img):
            os.remove(os.path.join(save_img, file))
    else:
        os.makedirs(save_img)

        
    headers = {
            "User-Agent": "Mozilla/5.0"
        }

    url = f"https://www.google.com/search?client=opera-gx&hs=N05&sca_esv=76076938c4eddbf2&q={query}&udm=2&fbs=AIIjpHxU7SXXniUZfeShr2fp4giZ1Y6MJ25_tmWITc7uy4KIetxLMeWi1u_d0OMRvkClUba76WL62NDKV-tuv6_wPYBC9v7ob7zIjaDzKC7u3qUzfD7e7YM11gPmU080OmUCW2ra6dnp670CRAaKtkLzGbsTDSqnsqGdRqpRgn7m8J8sRSSZQGr1gsZNygXo3gegFkXRGx97PLV94iHXkSHBuVAPRbU0rg&sa=X&ved=2ahUKEwiMo4jp2tSNAxW8dmwGHYz0MpEQtKgLegQICBAB&biw=722&bih=707&dpr=1.25"
    response=requests.get(url,headers=headers)
    soup=BeautifulSoup(response.content,'html.parser')

    img_file=soup.find_all('img')[1:11]
    image_files=[]
    index=0
    for img in img_file:
        img_src=img.get('src')
        try:
            image_data = requests.get(img_src).content
            filename = f"{index}.jpeg"
            with open(os.path.join(save_img,filename),'wb') as file:
                file.write(image_data)
            image_files.append(filename)
            index+=1
            
        except:
            continue
    return render_template("final.html", images=image_files, query=query)










if __name__ == "__main__":
    app.run(host='localhost', port=5000)