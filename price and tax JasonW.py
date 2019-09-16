item1 = input("please enter the price of item1:") #good
item2 = input("please enter the price of item2:")
item3 = input("please enter the price of item3:")
salestax = (float(item1)+float(item2)+float(item3))*0.12
total = (float(item1)+float(item2)+float(item3))*1.12
print("The total sales tax is ${0:.2f}".format(salestax))
print("The total cost is ${0:.2f}".format(total))
