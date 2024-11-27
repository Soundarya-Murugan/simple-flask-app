'''
Created on

@author: Soundarya

source:


    http://127.0.0.1:5000/reverse?name=Raji
'''

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():

    name = "Toronto"
    r_name = name[::-1]

    return f"Welcome to Toronto {r_name}"

@app.route("/reverse")
def reverse_name():

    name = request.values.get("name")
    r_name = name[::-1]

    return f"Your name is: {name}, your reverse name is: {r_name}"

@app.route("/user")
def get_user_details():

    name    = request.values.get("name")
    age     = request.values.get("age")

    return f"Your name is: {name}, your age is {age}"

# @app.route("/voting/eligibility")
# def get_voting_eligibility():

#     age     = int(request.values.get("age"))

#     content = ""
#     if age > 18:
#         content = "You are eligible to vote"
#     else:
#         content = "You are not eligible to vote"

#     return content

@app.route("/country", methods=["GET", "POST"])
def country():
    country = None
    capital = None
    error = None

    if request.method == "GET":
        country = request.args.get("country")
        
        if country:
            capitals = {
                'France'  : 'Paris',
                'Germany' : 'Berlin',
                'India'   : 'New Delhi'
            }

            capital = capitals.get(country)
            if not capital:
                error = "Country not found"
    
    return render_template("login.html", country=country, capital=capital, error=error)

if __name__ == "__main__":
    app.run(debug=True)