from turtle import *


#we want to paint a house
speed(15)
width(7)
color("red")
forward (200)
left(90)

forward (200)
left(90)

forward (200)
left(90)

forward (200)
left(90)
#end of square


#drawing a door
begin_fill()
forward (70)
color("green")
left(90)
forward (120)
right (90)
forward(60)
right(90)
forward(120)
right(90)
end_fill()

penup()
goto(200, 200)
pendown()
  

begin_fill() 
color("blue")
right(60)
forward(200)
left(120)
forward(200)
end_fill()


#windows 
 

penup()
goto(180,180)
pendown()
 
begin_fill()
color("blue")
left(30)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

penup()
goto(80,180)
pendown()

begin_fill()
color("blue")
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()





exitonclick()