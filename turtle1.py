import turtle

counter=1
while counter== 1:
    angle = float(input("Angle: "))
    length =float( input("Length: "))
    color = input("Color:")
    turtle.pencolor(color)
    turtle.left(angle)
    turtle.forward(length)
    if length ==0:
         counter = 0 
    
