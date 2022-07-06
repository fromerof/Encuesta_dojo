
from flask import render_template,redirect,request
from flask_app import app
from flask_app.models.dojo import Dojo

#HOME

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/create_dojo", methods=["POST"]) 
def create_dojo():
    if not Dojo.validate_survey(request.form):
        return redirect("/")
    Dojo.save(request.form)
    return redirect("/results")

@app.route("/results")
def results():
    result = Dojo.getSurvey()
    return render_template("result.html",result=result)




