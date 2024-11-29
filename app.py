from flask import Flask, session, redirect, request, render_template, url_for
import secrets 
from datetime import timedelta


app = Flask(__name__)

# app.secret_key  = os.getenv("SECREATE_KEY")
app.secret_key = secrets.token_hex(10)
# print (f"secret : {secrets.token_hex(10)}")
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes = 1)

@app.route('/', methods=['GET', 'POST'])
def login_page():
    
    if request.method == "POST":
        username = request.values.get("username")
        gender   = request.values.get("gender")
        age      = request.values.get("age")
    
        session['name']     = username
        session["age"]      = age
        session["gender"]   = gender
    
        return redirect(url_for("home"))

    return render_template("login.html")

@app.route('/welcome', methods=['GET', 'POST'])
def home():
    
    name = session.get("name")
    
    # age = session.get("age")
    
    print(f'session detils : {session}')

    return render_template(
        "welcome.html", 
        
        username=name
        )
    
@app.route('/get-user', methods=['GET'])
def get_user_details():
    
    user_dict = {
        "username": session.get("name"),
        "gender"  : session.get("gender"),
        "age"     : session.get("age")
    }
    
    return render_template(
        "user_details.html",
        
        user = user_dict,
        )
    

@app.route('/logout')
def session_logout():
    session.clear()
    return redirect(url_for("login_page"))



if __name__ == '__main__':
    app.run(
        debug=True, 
        port=4008
        )