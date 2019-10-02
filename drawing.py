import turtle
x=0
y=0
turtle.bgcolor("black")
    
def spiral(b,c,pen): #draw a spiral star
    turtle.pencolor(pen)
    turtle.speed(10)
    turtle.pu()
    turtle.setposition(b,c)
    turtle.pd()
    for i in range(20):
        turtle.forward(i * 10)
        turtle.right(144)
        
def star(x,y,color1,color2):
    turtle.pu()
    turtle.setposition(x,y) #set the position of the pen
    turtle.pd()
    turtle.color(color1,color2)
    
    turtle.begin_fill()
    counter=0
    while counter<5: #draw a star
        turtle.forward(200)
        turtle.right(144)
        counter=counter+1
    turtle.end_fill()

a=0
b=-300
def circle(a,b):
    turtle.pu()
    turtle.setposition(a,b) #set the position of the pen
    turtle.pd()
    turtle.color("brown","grey")
    turtle.begin_fill()
    turtle.circle(50) #draw the circle
    turtle.end_fill()

for circles in range (4): #duplicate the circle
    circle(a,b)
    a=a-100

turtle.ht()

    
    
spiral(400,-250,"white")
spiral(-500,-200,"blue")
star(-200,250,"yellow","red") #define the function
star(200,200,"blue","green")
star(-400,150,"purple","pink")
circle(0,-300)


