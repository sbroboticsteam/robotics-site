from flask import render_template, url_for
from sbrtsite import app

# Routes
@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', title='Home')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/mentorship")
def mentorship():
    return render_template('mentorship.html', title='Mentorship')

@app.route("/internalcomp")
def internalcomp():
    return render_template('internalcomp.html', title='Internal Competition')

@app.route("/sponsors")
def sponsors():
    return render_template('sponsors.html', title='Sponsors', sponsors=True)

@app.route("/contact")
def contact():
    return render_template('contact.html', title='Contact')

@app.route("/join")
def join():
    return render_template('join.html', title='Join The Team')

# Project Routes
@app.route("/projects/autocar")
def autocar():
    return render_template('autocar.html', title='AutoCar')

@app.route("/projects/rover")
def rover():
    return render_template('rover.html', title='Mars Rover')

@app.route("/projects/mechwarfare")
def mechwarfare():
    return render_template('mechwarfare.html', title='MechWarfare')