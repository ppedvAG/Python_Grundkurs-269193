from tkinter import *

window = Tk()
window.config(bg="blue")

l = Label(name="output")
l.place(x=10, y=10, width=100, height=20)

i = 0
def test():
	output = window.nametowidget("output")
	global i
	i += 1
	output.config(text=f"{i}")

b = Button(text="Zähler erhöhen")
b.place(x=10, y=40, width=100, height=20)
b.config(command=test)

window.mainloop()