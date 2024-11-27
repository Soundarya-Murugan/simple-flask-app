
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # You can change this to a more secure key

# Dummy user data (you can use a database in a real app)
users = {
    'testuser': 'password123'
}

@app.route('/')
def home():
    if 'username' in session:
        return f'Logged in as {session["username"]} <br><a href="/logout">Logout</a>'
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if the user exists and the password matches
        if username in users and users[username] == password:
            session['username'] = username  # Store username in session
            return redirect(url_for('home'))
        else:
            return 'Invalid credentials, please try again.'
    
    return render_template('logins.html')

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove the username from the session
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
