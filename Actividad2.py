from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
foodmovelist = [vector(0,10),vector(0,-10),vector(10,0),vector(-10,0)]
colorsSnake = ['#880C88','#0C885F','#AD7A0A','#2F0B8F', 'black']
colorsFood = ['#B49EF0','#9EE5F0','#BFF09E','#F0B89E','green']
snakeColor = 'black'
foodColor = 'green'


def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def insidef(food):
    "Return True if food inside boundaries."
    return -200 < food.x < 190 and -200 < food.y < 190

def move():
    global snakeColor,foodColor,colorsSnake,colorsFood
    "Move snake forward one segment."
    global food,foodmovelist
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        foodColor = colorsFood[randrange(0,5)]
        snakeColor = colorsSnake[randrange(0,5)]
    else:
        snake.pop(0)
        movement = foodmovelist[randrange(0,4)]
        food.move(movement)
    clear()
    if not insidef(food) and movement == foodmovelist[0]:
      food.move(foodmovelist[1])
    if not insidef(food) and movement == foodmovelist[1]:
      food.move(foodmovelist[0])
    if not insidef(food) and movement == foodmovelist[2]:
      food.move(foodmovelist[3])
    if not insidef(food) and movement == foodmovelist[3]:
      food.move(foodmovelist[2])
    
    for body in snake:
        square(body.x, body.y, 9, snakeColor)


    square(food.x, food.y, 9, 'green')
    square(food.x, food.y, 9, foodColor)

    update()
    ontimer(move, 100)
    

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
