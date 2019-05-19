import tkinter
print("To drow, hold down the left mouse button and move your mouse around.")
print("To change your brush colour, click on one of the colours.")
window = tkinter.Tk()
canvas = tkinter.Canvas(window, width = 750, height = 500, bg = "white")
canvas.pack()
lastX, lastY = 0,0
colour = "black"
def store_position(event):
  global lastX, lastY
  lastX = event.x
  lastY = event.y
def on_Click(event):
  store_position(event)
def on_drag(event):
  canvas.create_line(last, lastY, event.x, event.y, fill = colour, width = 3)
  store_position(event)
canvas.bind("<Button-1>",on_click)
canvas.bind("<B1-Motion>",on_drag)
window.mainloop()
