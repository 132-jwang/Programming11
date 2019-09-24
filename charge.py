cost = float(input("What is the total cost of your purchase? "))
country = input("Which country are you from? ")
tax1 = cost*1.05
tax2 = cost*1.13
tax3 = cost*1.11
if country == "Canada":
    province=input("Which province are you from? ")

    if province == "Alberta":
        print("Your total cost is ${0:.2f}".format(tax1)) 
    elif province == "Ontario" or "New Brunswick" or "Nova Scotia":
        print("Your total cost is ${0:.2f}".format(tax2))

    else:  print ("Your total cost is ${0:.2f}".format(tax3))

else: print("Your total cost is ${0:.2f}".format(cost))
    

    
