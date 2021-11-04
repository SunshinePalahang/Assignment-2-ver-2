def getappleQty():
    _appleQty = int(input("How many apple? "))
    return _appleQty

def getorangeQty():
    _orangeQty = int(input("How many orange? "))
    return _orangeQty

def gettotalAmount():
    apple_amount = int(20)*appleQty
    orange_amount = int(25)*orangeQty
    return apple_amount + orange_amount

def display(totalAmount):
    print(f"The total amount is {totalAmount}.")

appleQty = getappleQty()
orangeQty = getorangeQty()
totalAmount = gettotalAmount()
display(totalAmount)
