from flask import Flask, render_template, request
import requests

API_KEY = "dd9d7783ca1e37dfbe450e16dbab28de-de7062c6-65493037"
DOMAIN_NAME = "sandboxd172cd47aada453fb367e2d8bd137e31.mailgun.org"

app = Flask("Enquiries")

@app.route("/", methods=["POST"])
def sign_up():
    form_data = request.form
    print form_data["email"]

app.run(debug=True)
