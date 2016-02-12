from flask import render_template
from app import app 
import twitter_stream

@app.route('/')
@app.route('/index')
def index():
    response = twitter_stream.find_tweets()
    return render_template("index.html",response=response)