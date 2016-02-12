from flask import render_template, redirect
from app import app 
import twitter_stream

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/apology_counter", methods = ["POST"])
def apology_counter():
	return redirect("/apologies")

@app.route("/apologies")
def apologies():
	response = twitter_stream.find_tweets()
    	return render_template("apologies.html",response=response)