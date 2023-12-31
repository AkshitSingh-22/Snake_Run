import turtle
import time
import random
delay=0.1
wn=turtle.Screen()
wn.title("snake game by @AKHIT SINGH")
wn.bgcolor("green")
wn.setup(width=600,height=600)
wn.tracer(0)
#snake head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop"

def go_up():
    head.direction = "up"
    
def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"
    
def go_right():
    head.direction = "right"
    
#functions
def move():
    if head.direction == "up":
        y =head.ycor()
        head.sety(y+20)

    if head.direction == "down":
        y =head.ycor()
        head.sety(y-20)

    if head.direction == "left":
        x =head.xcor()
        head.setx(x-20)
        
    if head.direction == "right":
        x =head.xcor()
        head.setx(x + 20)

#Snake food

food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.penup()
food.goto(0,100)


segments = []



#Keyboard bindings

wn.listen()
wn.onkey(go_up, "s")
wn.onkey(go_down, "x")
wn.onkey(go_right, "d")
wn.onkey(go_left, "a")


#Main game loop
while True:
    wn.update()

    #Check for a collision with the border
    

    #check for collision with the food
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide the segments

        for segment in segments:
            segment.goto(1000, 1000)

        #clear the segments list
        segments.clear()
            

        

    if head.distance(food)<20:
        #Move the food to a random spot
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        #Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("purple")
        new_segment.penup()
        segments.append(new_segment)


    #Move the end segments first in reverse order
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    #Move segment 0 to where the head is
    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
                
    
        
    move()
    time.sleep(delay)

wn.mainloop()


