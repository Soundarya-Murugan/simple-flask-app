'''
Created on

@author: Soundarya

source:


    http://127.0.0.1:5000/reverse?name=Raji
'''

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():

    name = "Toronto"
    r_name = name[::-1]

    return f"Welcome to Toronto {r_name}"

# @app.route("/reverse")
# def reverse_name():

#     name = request.values.get("name")
#     r_name = name[::-1]

#     return f"Your name is: {name}, your reverse name is: {r_name}"

# @app.route("/user")
# def get_user_details():

#     name    = request.values.get("name")
#     age     = request.values.get("age")

#     return f"Your name is: {name}, your age is {age}"

# @app.route("/voting/eligibility")
# def get_voting_eligibility():

#     age     = int(request.values.get("age"))

#     content = ""
#     if age > 18:
#         content = "You are eligible to vote"
#     else:
#         content = "You are not eligible to vote"

#     return content

@app.route("/country")
def get_country_capital():
    
    capitals = {
        'France'  : 'Paris',
        'Germany' : 'Berlin' ,
        'India'   :  'New Delhi'
        
    }
   # Get the country name from the request arguments
    country = request.args.get("country")

    # Look up the capital and return it if it exists, otherwise return a message
    capital = capitals.get(country)
    if capital:
        return jsonify({"country": country, "capital": capital})
    else:
        return jsonify({"error": "Country not found"}), 404

if __name__ == '__main__':
    app.run(
        debug=True
    )