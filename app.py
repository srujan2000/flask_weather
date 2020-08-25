from flask import Flask,render_template,request,redirect,url_for
import requests
import json
import os

app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home():
	if request.method == "POST":
		city = request.form["city"]
		return redirect(url_for("cityname",usr = city))

	else:
		return render_template("search.html")


@app.route("/<usr>")
def cityname(usr): 
	try:
	  api_key = os.environ.get('openweather_apikey')
	  url = "http://api.openweathermap.org/data/2.5/weather?q="+usr+"&appid="+api_key+""
	  request_url= requests.get(url)
	  json_data= json.loads(request_url.content)
	  city=json_data['name']
	  temp= round(json_data['main']['temp'] -273,2)
	  humidity= json_data['main']['humidity']
	  clouds = json_data['clouds']['all']
	  condition = json_data['weather'][0]['description']
	  return render_template('details.html',content=[city,temp,humidity,clouds,condition])
	  # return f'{url}'
	except:
	  return render_template("search.html")	

if __name__ == "__main__":

	app.run(debug=True)