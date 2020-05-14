#!python3
# This is a coffee ordering page.
# The idea is to allow people to make orders in the office. 
# 

from flask import Flask, render_template, request
from coffeecalc import MyCoffee
import pymongo

app = Flask(__name__)

#

@app.route("/")
@app.route("/index")
def index():
  return render_template("base.html")

@app.route("/finalise", methods=["GET", "POST"])
def finalise():
  return "Hello"

@app.route("/order", methods=["GET", "POST"])
def order():
  global myTupleList
  if request.method == "POST":
    nameInput = request.form["nameInput"]
    email = request.form["email"]
    drinkType = request.form["drinkType"]
    milkType = request.form["milkType"]
    drinkSize = request.form["drinkSize"]
    sugarAmt = request.form["sugarAmt"]
    extras = request.form["extras"]
    myDrink = MyCoffee(drinkType, milkType, sugarAmt, extras,  drinkSize)
    myTuple = myDrink.returnData()
    # Add in the name and email
    toList = list(myTuple)
    toList.insert(0, email)
    toList.insert(0, nameInput)
    myTuple = tuple(toList)
    myTupleList.append(myTuple)
    return render_template("coffeelist.html", coffeeTuple = myTupleList)    
  else:
    myTupleList = []
    return render_template("order.html")


if __name__ == "__main__":
    app.run(debug=True)
