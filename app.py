from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Used to manage sessions

# Load association rules
rules = pd.read_csv("rules.csv")  # Assuming rules.csv contains the 'antecedents' and 'consequents'

# Route for Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Hardcoded credentials for login
        if email == "srinivasgd018@gmail.com" and password == "123456789":
            session["username"] = email
            return redirect(url_for("intro"))  # Redirect to the introduction page if login is successful
        else:
            return "Invalid email or password. Please try again."

    return render_template("login.html")

# Route for Introduction
@app.route("/intro")
def intro():
    if "username" not in session:
        return redirect(url_for("login"))  # Redirect to login if user is not logged in

    return render_template("introduction.html")

# Route for Index (where recommendations are shown)
@app.route("/", methods=["GET", "POST"])
def index():
    if "username" not in session:
        return redirect(url_for("login"))  # Redirect to login if user is not logged in

    recommendation = None
    if request.method == "POST":
        input_item = request.form.get("item")

        # Find the first matching rule where the input item is in 'antecedents'
        match = rules[rules["antecedents"].str.contains(input_item, case=False, na=False)]
        
        if not match.empty:
            recommendation = match.iloc[0]["consequents"]

    return render_template("index.html", recommendation=recommendation)

# Route for Logout
@app.route("/logout")
def logout():
    session.pop("username", None)  # Log the user out by removing the session
    return redirect(url_for("login"))  # Redirect to login page

if __name__ == "__main__":
    app.run(debug=True)
