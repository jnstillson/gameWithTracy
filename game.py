import turtle

#colors
colors = ['#E3C06E','#9CB16A','#5F9B72','#338178','#28646F','#2F4858',]
colors2 = ['#E79441', '#E27067', '#BD6085', '#835D8D', '#4C567B', '#2F4858']

def draw_shape(e1=5, e2=6, l1=10, l2=10, col=colors2):
    for t in range(e2):

        tracy.begin_fill()
        tracy.fillcolor(col[t % len(col)])
        tracy.pencolor(col[t % len(col)])
        for n in range(e1):
            tracy.forward(l1)
            tracy.left(720 / e1)

        tracy.end_fill()

        tracy.up()
        tracy.forward(l2)
        tracy.left(360 / e2)
        tracy.down()

    return

#creates window
window = turtle.Screen()
window.colormode(255)

#creates turtle
tracy = turtle.Turtle()
tracy.speed(0)


#ask user
f = int(input('How many flowers: '))

#do stuff

#number of edges in the 'petals', it will cycle through different numbers if you add them to the list
edges = [3]
#length (X10) of the edges in the 'petals', it will also cycle through
sizes = [1,2,3,4,5]
#color set used for each flower
cols = [colors, colors2]

#each time it draws a full flower here (code for individual flower is under draw_shape
for flower in range(f):
    draw_shape(e1=edges[flower%len(edges)], #this takes the number of edges in the petals from the list above
               l1=10*sizes[((flower+1)%len(sizes))], #same for the length of the petal sides
               col=cols[flower%len(cols)]) #same for the color
    tracy.up()
    tracy.right(360/f)
    tracy.forward(100)
    tracy.down()

#end/exit
turtle.exitonclick()
