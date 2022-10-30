import tkinter
import time
from Balls import Ball

window = tkinter.Tk()

WIDTH = 500
HEIGHT = 500

canvas = tkinter.Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

rectangle = canvas.create_rectangle(2, 2, WIDTH - 1, HEIGHT - 1)

ball_1 = Ball(canvas, 10, 10, 100, 1, 1, 'red')
ball_2 = Ball(canvas, 0, 0, 50, 4, 3, "blue")

while True:
    ball_1.move_ball()
    ball_2.move_ball()
    window.update()
    time.sleep(0.01)


window.mainloop()
