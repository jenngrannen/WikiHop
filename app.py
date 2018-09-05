from Wikihop import *
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/wikihop", methods=["POST"])
def search():
    startURL = request.form.get("startURL")
    endURL = request.form.get("endURL")
    depth = request.form.get("depth")
    list = runIt(startURL, endURL, int(depth))
    if not startURL or not endURL or not depth:
        return render_template("failure.html")
    if list == None:
        return render_template("noPath.html")
    return render_template("results.html", list=list)

@app.route("/back", methods=["POST"])
def back():
    return redirect(url_for('index'))
