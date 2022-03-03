import turtle
import os
from xmlrpc.server import DocXMLRPCRequestHandler
#Ekran, background
ggs = turtle.Screen()
ggs.setup(width=800, height=600)
ggs.title('Ping pong :]')
ggs.bgcolor('black')
ggs.tracer(0)

#Rakietka nr 1
rakietka_1 = turtle.Turtle()
rakietka_1.shape("square")
rakietka_1.color('white')
rakietka_1.shapesize(stretch_len=1, stretch_wid=5)
rakietka_1.penup()
rakietka_1.goto(-350,0)
rakietka_1.speed(0)

#Rakietka nr 2
rakietka_2 = turtle.Turtle()
rakietka_2.shape("square")
rakietka_2.color('white')
rakietka_2.shapesize(stretch_len=1, stretch_wid=5)
rakietka_2.penup()
rakietka_2.goto(350,0)
rakietka_2.speed(0)

#winik
grasz_1 = 0
gracz_2 = 0

#Pilka
pilka = turtle.Turtle()
pilka.shape("square")
pilka.color('white')
pilka.penup()
pilka.goto(0,0)
pilka.speed(0)
pilka.dx = 0.25
pilka.dy = pilka.dx

##
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Gracz 1: 0  Gracz 2: 0", align="center", font=("Courier", 24, "normal"))

#kontrola
def rakietka_1_up():
	y = rakietka_1.ycor()
	y += 20
	rakietka_1.sety(y)
def rakietka_1_down():
    y = rakietka_1.ycor()
    y -= 20
    rakietka_1.sety(y)

def rakietka_2_up():
    y = rakietka_2.ycor()
    y += 20
    rakietka_2.sety(y)

def rakietka_2_down():
    y = rakietka_2.ycor()
    y -= 20
    rakietka_2.sety(y)

ggs.listen()
ggs.onkeypress(rakietka_1_up, "w")
ggs.onkeypress(rakietka_1_down, "s")
ggs.onkeypress(rakietka_2_up, "Up")
ggs.onkeypress(rakietka_2_down, "Down")

#loop
while True:
    ggs.update()
    
    # ruch pilki
    pilka.setx(pilka.xcor() + pilka.dx)
    pilka.sety(pilka.ycor() + pilka.dy)

    # uderzenie pilki o gore i dol
    if pilka.ycor() > 290:
        pilka.sety(290)
        pilka.dy *= -1
        os.system("afplay bounce.wav&")
    
    elif pilka.ycor() < -290:
        pilka.sety(-290)
        pilka.dy *= -1
        os.system("afplay bounce.wav&")

    # punktacja gdy pilka wypadnie z gry
    if pilka.xcor() > 370:
        grasz_1 += 1
        pen.clear()
        pen.write("Gracz 1: {}  Gracz 2: {}".format(grasz_1, gracz_2), align="center", font=("Courier", 24, "normal"))
        pilka.goto(0, 0)
        pilka.dx *= -1

    elif pilka.xcor() < -370:
        gracz_2 += 1
        pen.clear()
        pen.write("Gracz 1: {}  Gracz 2: {}".format(grasz_1, gracz_2), align="center", font=("Courier", 24, "normal"))
        pilka.goto(0, 0)
        pilka.dx *= -1

    #Gdy rakietka uderzy pilke
    if pilka.xcor() < -340  and pilka.ycor() < rakietka_1.ycor() + 50 and pilka.ycor() > rakietka_1.ycor() - 50:
        pilka.dx *= -1 
        os.system("afplay bounce.wav&")
    
    elif pilka.xcor() > 340 and pilka.ycor() < rakietka_2.ycor() + 50 and pilka.ycor() > rakietka_2.ycor() - 50:
        pilka.dx *= -1
        os.system("afplay bounce.wav&")

	#Gdy rakietka udzerzy pilke bokiem 
