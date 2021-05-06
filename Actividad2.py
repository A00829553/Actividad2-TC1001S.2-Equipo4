# Autores:
# Roberto Miguel Rodriguez Hermann A00829553
# Luis Carlos Balderrama Espinoza A00226908
'''
Conclusión Luis Carlos: en lo personal nunca he programado mas que cosas muy basicas hace un año y medio que como no necesite ya se me habian olvidado 
y lograr retomar algunas de esas cosas y poder realizar mi parte es muy satisfactorio y creo que comprendo al menos mas que antes como funciona programar.

Conclusion Roberto: Me parece bastante interesante las tecnicas usadas para simular movimiento dentro de nuestro juego.
Creo que con estas tecnicas podemos llegar a hacer proyectos bastantes interesantes
'''

#Imports de las librerias requeridas
from turtle import *
from random import randrange
from freegames import square, vector

#Declaracion de variables globales que vamos a estar utilizando
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
    "Move snake forward one segment."
    #Declaracion de las variables globales que requerimos
    global snakeColor,foodColor,colorsSnake,colorsFood,food,foodmovelist
    
    #Creacion de la cabeza
    head = snake[-1].copy()
    head.move(aim)

    #Chequeo para ver si no se ha perdido
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    #Chequeo para ver si se comio o no la comida, sino la comida se mueve
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
    
    #Chequeo para que la comida no salga de la zona designada
    if not insidef(food) and movement == foodmovelist[0]:
      food.move(foodmovelist[1])
    if not insidef(food) and movement == foodmovelist[1]:
      food.move(foodmovelist[0])
    if not insidef(food) and movement == foodmovelist[2]:
      food.move(foodmovelist[3])
    if not insidef(food) and movement == foodmovelist[3]:
      food.move(foodmovelist[2])
    
    #Loop para dibujar la serpiente
    for body in snake:
        square(body.x, body.y, 9, snakeColor)

    #Dibujo de la comida
    square(food.x, food.y, 9, foodColor)

    #Funciones para poder seguir actualizando el juego
    update()
    ontimer(move, 100)
    
#Funciones principales
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
#Controles para moverse
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
