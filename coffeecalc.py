# This unit will return a tuple with the coffee type and price:
# e.g. ("Flat White", "Full Cream", "Extra Shot x 1", "One Sugar", "Large", 5.7)

coffeeData = {
  "espresso320": { "name": "Espresso", "price" : 3.2 },
  "shortmac360": {"name": "Short Mac", "price" : 3.6},
  "cappucino400": {"name": "Cappucino", "price": 4.0},
  "flatwhite400": {"name": "Flat White", "price" : 4.0},
  "latte400": {"name": "Latte", "price" : 4.0},
  "longblack400": {"name": "Long Black", "price" : 4.0},
  "affogato440": {"name": "Affogato", "price": 4.4},
  "longmac440": {"name": "Long Mac", "price": 4.4},
  "mocha440": {"name": "Mocha", "price": 4.4},
  "hotchocolate440": {"name": "Hot Chocolate", "price": 4.4},
  "chailatte440": {"name": "Chai Latte", "price": 4.4},
  "vienna440": {"name": "Vienna", "price": 4.4},
  "turmeric450": {"name": "Turmeric", "price": 4.5},
  "matchalatte450": {"name": "Matcha Latte", "price": 4.5},
  "icedlatte570": {"name": "Iced Latte", "price": 5.7},
  "icedblackcoffee540": {"name": "Iced Black Coffee", "price": 5.4},
  "icedcoffee650": {"name": "Iced Coffee", "price": 6.5},
  "icedmocha650": {"name": "Iced Mocha", "price": 6.5},
  "icedchoc650": {"name": "Iced Choc", "price": 6.5},
  "icedchai650": {"name": "Iced Chai", "price": 6.5}
}

milkData = {
    "none": {"name": "No Milk", "price": 0},
    "fullcreammilk": {"name": "Full Cream", "price": 0},
    "hilomilk": {"name": "Hi-Lo", "price": 0},
    "skimmilk": {"name": "Skim Milk", "price": 0},
    "soymilk60": {"name": "Soy Milk", "price": 0.6},
    "almondmilk60": {"name": "Almond Milk", "price": 0.6}
}

extrasData = {
    "none": {"name": "No Extras", "price": 0},
    "syrup": {"name": "Syrup", "price": 0.6},
    "xshot1": {"name": "Extra Shot x 1", "price":  0.6},
    "xshot2": {"name": "Extra Shot x 2", "price":  1.2},
    "decaf": {"name": "Decaf", "price":  0.4}
  }

sugarData = {
    "sugarNone": "No Sugar",
    "sugarOne": "One Sugar",
    "sugarTwo": "Two Sugars",
    "sugarThree": "Three Sugars",
    "sugarFour": "Four Sugars" 
}

sizeData = {
    "coldDrink": {"name": "Cold Drink", "price":  0.0},
    "small": {"name": "Small", "price":  0.0},
    "medium": {"name": "Medium", "price":  1.0},
    "large": {"name": "Large", "price":  2.0}
}

class MyCoffee():
  def __init__(self, myCoffee, myMilk,  mySugar, myExtras, mySize):
    self.myCoffee = coffeeData[myCoffee]["name"]
    self.myMilk = milkData[myMilk]["name"]
    self.myExtras = extrasData[myExtras]["name"]
    self.mySugar = sugarData[mySugar]
    self.mySize = sizeData[mySize]["name"]
    self.myCost = coffeeData[myCoffee]["price"] + milkData[myMilk]["price"] + \
        extrasData[myExtras]["price"] + sizeData[mySize]["price"]

  def returnData(self):
    return(self.myCoffee, self.myMilk, self.mySugar, self.myExtras, self.mySize, round(self.myCost, 2))
