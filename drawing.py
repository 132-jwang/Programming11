import turtle
x=0
y=0
def star(x,y,color1,color2):
    turtle.speed(10)
    turtle.pu()
    turtle.setposition(x,y) #set the position of the pen
    turtle.pd()
    turtle.color(color1,color2)
    
    turtle.begin_fill()
    for i in range(5): #draw a star
        turtle.forward(200)
        turtle.right(144)
    turtle.end_fill()

a=0
b=0
def trig(a,b,co1,co2):
    turtle.pu()
    turtle.setposition(a,b) #set the position of the pen
    turtle.pd()
    turtle.color(co1,co2)
    counter=0
    turtle.begin_fill()
    while counter <3: #draw a triangle
        turtle.right(120)
        turtle.forward(100)
        counter=counter+1
    turtle.end_fill()
    
    

star(-200,250,"yellow","red") #define the function
star(200,200,"blue","green")
star(-400,250,"purple","pink")
trig(0,-100,"brown","black")
