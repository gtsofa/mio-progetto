# views.py

from flask import render_template

from app import app

@app.route('/')
def index():
    """points to home page ie index"""
    return render_template("index.html")
    
@app.route('/about')
def about():
    """points to the about page"""
    return render_template("about.html")