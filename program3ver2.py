def getrawAmount():
    rawAmount = int(input("Enter your amount of money: "))
    return rawAmount

def getpriceApple():
    priceApple = int(input("Enter the price of apple: "))
    return priceApple

def getquantityApple():
    quantityApple =int(raw_amount/price_apple)
    return quantityApple

def gettotalPayment():
    totalPayment = int(price_apple*quantity_apple)
    return totalPayment

def gettotalAmount():
    totalAmount = int(raw_amount%total_payment)
    return totalAmount




raw_amount = getrawAmount()
price_apple = getpriceApple()
quantity_apple = getquantityApple()
total_payment = gettotalPayment()
total_amount = gettotalAmount()
