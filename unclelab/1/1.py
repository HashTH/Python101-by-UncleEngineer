import turtle
tao = turtle.Pen()
col = ['purple','pink','#9932CC','#87CEEB','#800000',
       '#7FFFD4','#9ACD32','#FFB6C1','#D8BFD8','#556B2F']
tao.speed(0)
for i in range(10):
    tao.color(col[i])
    tao.circle(i*36)
    tao.penup()
    tao.forward(10)
    tao.right(36)
    tao.pendown()