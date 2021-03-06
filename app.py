from flask import Flask, render_template, request
from dotenv import load_dotenv
import requests

app = Flask("finalappproject")

@app.route("/")
def home_page():
	return render_template("index.html")

@app.route("/photo", methods=['POST'])
def photo():
    date = request.form["date"]
    name = request.form["name"] 
    your_key = 'WHZtatGGJ3iVUyZDPLuOSlnTxAcZQgWVMlSG3fLf'
    url = 'https://api.nasa.gov/planetary/apod'
    payload = {"api_key": your_key,"date": date}
	
    response = requests.get(url, params=payload)
	
    nasa_img_of_day_data = response.json()
	
    img_expl = nasa_img_of_day_data['explanation']
    img_title = nasa_img_of_day_data['title']
    img_url = nasa_img_of_day_data['url']

    return render_template("index.html", explanation=img_expl, title=img_title, image=img_url)

app.run(debug=True)