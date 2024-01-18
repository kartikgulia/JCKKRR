from flask import Flask, render_template


app = Flask(__name__)


@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/login")
def home():
    return render_template("login.html")

@app.route("/signup")
def home():
    return render_template("signup.html")


@app.route("/")
def home():
    return render_template("splash.html")
