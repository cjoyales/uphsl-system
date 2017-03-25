#!/usr/bin/evn python3

from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template('login.html')