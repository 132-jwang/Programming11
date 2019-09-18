
amount=float(input("What is the total amount of your purchase? "))
shipping =amount+10
if amount>=50 :
    print("Your total cost is ${0:.2f}".format(amount))
else:
    print("Your total cost is ${0:.2f}".format(shipping))

    
    
