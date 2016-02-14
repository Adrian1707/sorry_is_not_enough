from flask import Flask, session, redirect, url_for, escape, request, render_template
from app import app 
import twitter_stream
import os

@app.route('/')
def index():
	if 'response' in session:
		response=session['response']
    		return render_template("index.html",response=response)
    	return render_template("index.html")


@app.route("/apology_counter", methods = ["POST"])
def apology_counter():
	session['response'] = twitter_stream.find_tweets()
	return redirect("/")

# @app.route("/apologies")
# def apologies():
# 	response = twitter_stream.find_tweets()
#     	return render_template("apologies.html",response=response)

app.secret_key = os.urandom(32)