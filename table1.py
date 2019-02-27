from flask import Flask,render_template

table1=Flask(__name__)

@app.route("/")

def index():
    return render_template("logpage.html")

if(__name__=="__main__"):
    table1.run(debug=True)