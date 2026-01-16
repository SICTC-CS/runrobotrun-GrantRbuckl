#   a115_robot_maze.py
import turtle as trtl

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

#----- map variables
current = 0
maze1map = [[0,0,0,0,2],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [3,0,0,0,0]]



#------ robot commands
def up():
  robot.dot(10)
  robot.seth(90)
  robot.fd(50)

def checkLoc(dir):
  global current
  if dir == up:
    if 3 in maze1map[1]:
      
      
  
  

def turn_left():
  robot.speed(0)
  robot.lt(90)
  robot.speed(2)

def turn_right():
  robot.speed(0)
  robot.rt(90)
  robot.speed(2)

#----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "robot.gif"
wn.addshape(robot_image)

#----- init robot
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()

#---- TODO: change maze here
wn.bgpic("maze1.png") # other file names should be maze2.png, maze3.png

#---- TODO: begin robot movement here
# move robot forward with move()
# turn robot left with turn_left()
# sample for loop:
'''
for step in range(3): # forward 3
  move()
'''
#Maze 1
for i in range(4):
  move()
robot.rt(90)
for i in range(4):
  move()

#---- end robot movement 
wn.mainloop()
