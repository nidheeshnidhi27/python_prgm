from flask import Flask,render_template

TABLE=Flask(__name__)

@app.route("/")

def index():
    return render_template("logpage.html")

if(__name__=="__main__"):
    app.run(debug=True)