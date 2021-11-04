def getrawAmount():
    rawAmount = int(input("Enter your amount of money: "))
    return rawAmount

def getpriceApple():
    priceApple = int(input("Enter the price of apple: "))
    return priceApple



def display(quantity_apple, total_amount):
    print(f"You can buy {quantity_apple} apples and your change is {total_amount} pesos.")


raw_amount = getrawAmount()
price_apple = getpriceApple()
