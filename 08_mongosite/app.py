#Britni Canale
#SoftDev1 pd 6
#K26 -- Getting More REST
#2018-11-15


from flask import Flask, render_template, session, request, url_for, redirect, flash, jsonify
from util import nobelprize

app = Flask(__name__)

@app.route("/")
def hello():
    nobelprize.insertData()
    return render_template("index.html")

@app.route("/results")
def search():
    thing = ""
    if "IP" in request.args:
        print(f"this is ip : {request.args.get('IP')}")
        nobelprize.insertData()
        nobelprize.changeIP(request.args.get("IP"))
    if "topic" in request.args:
        print(f"topic chosen: {request.args.get('topic')}")
        thing = nobelprize.find_year(request.args.get("topic"))
    print(thing)
    return render_template("results.html", res=thing)

if __name__ == "__main__":
    app.debug = True
    app.run()
