# import flask
from flask import Flask, jsonify, redirect, url_for, render_template

# create an instance of our app
app = Flask(__name__)

@app.errorhandler(404)
def handle_not_found(error):
    return redirect(url_for("About"))

# @app.route("/")
# def Default():
#     return render_template("Default.html")

@app.route("/")
def About():
    return render_template("About.html")

@app.route("/Experience")
def Experience():
    return render_template("Experience.html")

@app.route("/Education")
def Education():
    return render_template("Education.html")

@app.route("/Projects")
def Projects():
    return render_template("Projects.html")

if __name__ == '__main__':
	app.run()