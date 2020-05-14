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

@app.route("/order", methods=["GET", "POST"])
def order():
  if request.method == "POST":
    drinkType = request.form["drinkType"]
    milkType = request.form["milkType"]
    drinkSize = request.form["drinkSize"]
    sugarAmt = request.form["sugarAmt"]
    extras = request.form["extras"]
    myDrink = MyCoffee(drinkType, milkType, extras, sugarAmt, drinkSize)
    myTuple = myDrink.returnData()
    return(f"{myTuple}")
  else:
    return render_template("order.html")

if __name__ == "__main__":
    app.run(debug=True)
