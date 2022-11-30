from tkinter import *
from random import *
from tkinter import colorchooser

size = 2600.0
root = Tk()
root.overrideredirect(1)
root.state('zoomed')
canvas = Canvas(root, width=size, height=size)
canvas.pack()
diapason = 0

#def exit(event): root.destroy()
while True:
    colors = choice(['aqua', 'blue', 'fuchsia', 'green', 'maroon', 'orange',
                     'pink', 'purple', 'red', 'yellow', 'violet', 'indigo', 'chartreuse', 'lime'])
    x0 = randint(-30, size)
    y0 = randint(-30, size)
    d = randint(1, size / 260)
    canvas.create_oval(x0, y0, x0 + d, y0 + d, fill=colors)
    root.bind('<Button-1>', exit)
    root.bind('<Return>', exit)
    #root.mainloop() основа   32522

    root.update()



