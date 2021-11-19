from flask import Blueprint, request, url_for, redirect, render_template, flash, jsonify
from .models import ExampleClass
import json

web = Blueprint('web', __name__, template_folder="templates", static_folder="static")

@web.route("/")
def home():
    currentTime = ExampleClass()
    currentTime.giveMeTime()
    return render_template('index.html', currentTime = currentTime.currentTime)

#@web.route("/time")
#def showTime():
#    currentTime = ExampleClass()
#    currentTime.giveMeTime()
#    return jsonify(result=currentTime.currentTime)

@web.route("/jotason")
def showTime():
    myjson = json.loads('{"mykey": "myvalue"}')
    resultado = json.dumps(myjson)
    return jsonify(result=resultado)
