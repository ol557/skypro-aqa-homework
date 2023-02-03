from turtle import *

my_turtle = Turtle()
my_turtle.speed(0)
my_turtle.screen.setup(1200, 800)

# нарисовать квадрат
#def draw_rect(t):
    #for x in range(0, 4):
        #t.right(90)
        #t.forward(180)

# рисует квадраты в цикле
#for x in range(0, 1):
    #draw_rect(my_turtle)
    #my_turtle.right(1)
    

my_turtle.circle(70)
my_turtle.up()
my_turtle.goto(105, 55)
my_turtle.down()
my_turtle.circle(40)
my_turtle.up()
my_turtle.goto(-105, 55)
my_turtle.down()
my_turtle.circle(40)

my_turtle.up()
my_turtle.goto(-30, 80)
my_turtle.down()
my_turtle.circle(7)
my_turtle.up()
my_turtle.goto(30, 80)
my_turtle.down()
my_turtle.circle(7)

my_turtle.up()
my_turtle.goto(-20, 35)
my_turtle.down()
my_turtle.right(45)
my_turtle.circle(30, 90)

my_turtle.up()
my_turtle.goto(0, 70)
my_turtle.down()
my_turtle.right(90)
my_turtle.forward(15)
my_turtle.right(135)
my_turtle.forward(20)
my_turtle.right(135)
my_turtle.forward(15)
my_turtle.ht()



# необходимо, чтобы окно не закрывалось само, а только по клику
my_turtle.screen.exitonclick()
my_turtle.screen.mainloop()

