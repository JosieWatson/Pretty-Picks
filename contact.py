from flask import Flask, render_template, request, redirect
import requests
import os

app = Flask("enquiries")
port = int(os.environ.get("PORT", 5000))
weather_API_KEY = "1a312c59889287b348f170efadcb790e"

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/dressme")
def dressme():
    return render_template("dressme.html")

@app.route("/signup", methods = ["POST"])
def signup():
    email = request.form["email"]
    enquiry = request.form["enquiry"]
    print("The email address is '" + email + "', enquiry is '" + enquiry + "'")
    return redirect("/")

@app.route("/OOtD", methods = ["POST"])
def weather():
    location = request.form["location"]
    endpoint = "http://api.openweathermap.org/data/2.5/weather"
    payload = {"q": location, "units": "metric", "appid": weather_API_KEY}
    response = requests.get(endpoint, params=payload)
    data = response.json()
    temperature = data["main"]["temp"]
    if temperature >= 20 < 30:
        return render_template("hot.html")
    elif temperature >= 10 < 20:
        return render_template("moderate.html")
    elif temperature >= 0 < 10:
        return render_template("cool.html")
    elif temperature >= -10 < 0:
        return render_template("cold.html")
    else:
        return render_template("inside.html")


#cse_id = os.environ.get("cse_id", None)
#api_key = os.environ.get("api_key", None)

#gis = GoogleImagesSearch('api_key', 'cse_id')

#_search_params = {
#    'q': '...',
#    'num': 1-50,
#    'safe': 'high',
#    'fileType': 'jpg|gif|png',
#    'imgType': 'photo',
#    'imgSize': 'medium',
#    'searchType': 'image',
#    'imgDominantColor': ''
#}

#gis.search({'q': 'boho', 'num': 3})

app.run(host='0.0.0.0', port=port, debug=True)
