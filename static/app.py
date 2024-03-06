from flask import Flask, render_template


app = Flask(__name__)


@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/")
def route():
    return render_template("splash.html")

@app.route("/picClick")
def picClick():
    return render_template("picClick.html")