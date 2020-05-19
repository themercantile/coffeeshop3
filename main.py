#!python3
# This is a coffee ordering page.
# The idea is to allow people to make orders in the office. 

from flask import Flask, render_template, request, session
from coffeecalc import MyCoffee
import datetime
import pymongo

#connecting to my mongodb atlas db
'''
myClient = pymongo.MongoClient("mongodb+srv://numbat:dfjQUGz09AFtm5AY@cluster0-su57x.mongodb.net/test?retryWrites=true&w=majority",
                             connectTimeoutMS=30000, socketTimeoutMS=None, socketKeepAlive=True, connect=False, maxPoolsize=1)

password is myNDIScoffeeapp ndiscoffee@gmail.com                      
'''
myClient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myClient["coffeedatabase"]
# "coffee_orders" is what the database will be called on the server
coffeeDocument = mydb["coffee_orders"]
# "coffeeDocument" is a json document used in pymongo database

app = Flask(__name__)

app.secret_key = "secret covfefe key"

@app.route("/")
@app.route("/index")
def index():
  return render_template("base.html")

@app.route("/finalise", methods=["GET", "POST"])
def finalise():
  myTupleList=session['orderTuple']
  print(myTupleList) # this is for debugging
  dbWrite(myTupleList)  
  return render_template("finalise.html", coffeeTuple=myTupleList)

@app.route("/admin")
def admin():
  coffeeDict = []
  myTupleList = []
  # This view is for the admin to view the orders. It will retrieve the orders then convert the table to a PDF then email it.
  # There will be no link to this page yet.
  coffeeCursor = dbRead()
  for line in coffeeCursor:
    coffeeDict.append(line)
  # print(coffeeDict)
  for line in coffeeDict:
    myTuple = (line['name'], line['email'], line['drinktype'], line['milkType'], line['sugarAmt'], line['extras'], line['drinkSize'], line['price'])
    myTupleList.append(myTuple)  
  return render_template("admin.html", coffeeTuple = myTupleList)


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
    session['orderTuple'] = myTupleList
    return render_template("coffeelist.html", coffeeTuple = myTupleList)    
  else:
    myTupleList = []
    # Lines with time functions are to determine if it's too late to make an order. Will allow midnight to 9.59AM
    now = datetime.datetime.now()
    if (int(now.strftime("%H")) > 23):
      return "Orders end at 10AM - Sorry!"
    else:
      return render_template("order.html")

# write to database
def dbWrite(myTupleList):
  coffeeDict = []
  now = datetime.datetime.now()
  nowstr = now.strftime("%Y%m%d")  # E.g. 20200518 <-- 2020 05 18
  for myTuple in myTupleList:
    #create list of dics to write to db
    coffeeDict.append({"date": nowstr, "name": myTuple[0], "email": myTuple[1], "drinktype": myTuple[2], "milkType": myTuple[3], 
                      "sugarAmt": myTuple[4], "extras": myTuple[5], "drinkSize": myTuple[6], "price": myTuple[7]})
  # print(coffeeDict) for debugging purposes
  x = coffeeDocument.insert_many(coffeeDict) #write to database

def dbRead():
  coffeeDict = []
  now = datetime.datetime.now()
  nowstr = now.strftime("%Y%m%d")  # E.g. 20200518 <-- 2020 05 18
  dbQuery = { "date": nowstr } # find all the lines which have today's date in them
  coffeeDict = coffeeDocument.find(dbQuery)
  return coffeeDict

if __name__ == "__main__":
    app.run(debug=True)