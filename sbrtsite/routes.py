from flask import render_template, url_for
from ___init___ import app

# Routes
@app.route("/")
@app.route("/home")
def home():
    return render_template()

@app.route("/about")
def about():
    return render_template()

@app.route("/mentorship")
def mentorship():
    return render_template()

@app.route("/internalcomp")
def internalcomp():
    return render_template()

@app.route("/sponsors")
def sponsors():
    return render_template()

@app.route("/contact")
def contact():
    return render_template()

@app.route("/join")
def join():
    return render_template()

# Project Routes
@app.route("/projects/autocar")
def autocar():
    return render_template()

@app.route("/projects/rover")
def rover():
    return render_template()

@app.route("/projects/mechwarfare")
def mechwarfare():
    return render_template()