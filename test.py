import requests
import json

name=input()

url = "http://api.openweathermap.org/data/2.5/weather?q="+str(name)+"&appid=dec475c4b2c1ae00f28d29ff29846d77"

try:
	request_url= requests.get("http://api.openweathermap.org/data/2.5/weather?q="+str(name)+"&appid=dec475c4b2c1ae00f28d29ff29846d77")
	json_data= json.loads(request_url.content)
	city=json_data['name']
	temp= round(json_data['main']['temp'] -273,2)
	humidity= json_data['main']['humidity']
	clouds = json_data['clouds']['all'];
	condition = json_data['weather'][0]['description'];

	print(city,temp,humidity,clouds,condition)

except Exception as e:
	print(e)