import turtle

#creates window
window = turtle.Screen()
window.colormode(255)

#creates turtle
tracy = turtle.Turtle()

#colors
colors = ['#E3C06E','#9CB16A','#5F9B72','#338178','#28646F','#2F4858']

#ask user for edge number
edge1 = int(input('How many edges: '))
length1 = float(input('How far: '))
edge2 = int(input('How many edges again: '))
length2 = float(input('How far again: '))

#do stuff
for t in range(edge2):

    tracy.begin_fill()
    tracy.fillcolor(colors[t % len(colors)])
    tracy.pencolor(colors[t % len(colors)])
    for n in range(edge1):
        tracy.forward(length1)
        tracy.left(360 / edge1)

    tracy.end_fill()

    tracy.up()
    tracy.forward(length2)
    tracy.left(360/ edge2)
    tracy.down()

#end/exit
turtle.exitonclick()
