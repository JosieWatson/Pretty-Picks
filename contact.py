from flask import Flask, render_template, request, redirect
import os

app = Flask("enquiries")
port = int(os.environ.get("PORT", 5000))

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/signup", methods = ["POST"])
def signup():
    email = request.form["email"]
    enquiry = request.form["enquiry"]
    print("The email address is '" + email + "', enquiry is '" + enquiry + "'")
    return redirect("/")

app.run(host='0.0.0.0', port=port, debug=True)

#Custom search - if we can get it to work!
#from flask import Flask
#from google_images_search import GoogleImagesSearch
#import os

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

#gis.search(_search_params=_search_params)
