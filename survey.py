import smtplib
import imaplib
import poplib
import time
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return "i dont really know"

app.run(host="0.0.0.0", port=80)

@app.route('/submit', methods=["POST"])
def submit():
    # The following variables are getting info from the submitted form
    # Saving them so that it can use that info when submitting the SQL statement
    pname = request.form["pname"]
    email = request.form["email"]
    uniform = request.form["uniform"]
    patches = request.form["patches"]
    class_age = request.form["class_age"]
    attendance = request.form["attendance"]



# input("Parent Name: ")
# input("Student(s) name(s)")
# input("Prefered email adress: ")
# input("Number of uniforms: ")
# input("Number of patches: ")
# input("Which class does your child attend? ")
# input("What days do your students go to class? ")

