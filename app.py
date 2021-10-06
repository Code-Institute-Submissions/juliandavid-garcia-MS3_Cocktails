import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)



app = Flask(__name__)

app.config["MONGO_DBNAME"]= os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")



@app.route("/")
@app.route("/index")
def index(): 
    return render_template("index.html")



@app.route("/login")
def login(): 
    return render_template("login.html")


@app.route("/logout")
def logout(): 
    return render_template("logout.html")


@app.route("/register")
def register(): 
    return render_template("register.html")


if __name__=="__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)