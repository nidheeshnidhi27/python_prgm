from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")

def index():
    return render_template("logpage.html")

@app.route("/main")

def home():
    return render_template("student.html")

@app.route("/home")

def details():
    return "nidheesh"

@app.route("/about")

def about():
    return "mca"

@app.route("/contact")

def mobile():
    return "mobile number"

@app.route("/new")

def new():
    return "exit"

@app.route("/demoo")

def demo():
    return "my program"

if(__name__=="__main__"):
    app.run(debug=True)
