from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
# <turtle.Turtle object at 0x00000270582C6550>
timmy.shape('turtle')
timmy.color('Blue')
timmy.forward(100)
timmy.circle(123)




my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()