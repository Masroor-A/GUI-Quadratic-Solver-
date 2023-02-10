from tkinter import *
from math import sqrt

background = "#1a659e"
orange = "#ff6b35"
blue = "#0076C9"

root = Tk()
root.config(background=background)
root.geometry("300x550")
root.title("Quadratic Solver")


def Solve():
	root2 = Tk()
	root2.title("Answer")
	root2.config(background=background)
	a = float(A.get())
	b = float(B.get())
	c = float(C.get())
	discriminent = (b**2) - (4*a*c)

	if discriminent < 0:
		label = Label(root2, text="This Function Is Fnfactorable", background=background, foreground=orange, font=("Arial", 15, "bold"))

		label.pack()
	else:
		discriminent = sqrt((b**2) - (4*a*c))
		x1 = ((-1*b)+ discriminent)/(2*a)
		x2 = ((-1*b)- discriminent)/(2*a)
		label = Label(root2, text="Your Zeros are", background=background, foreground=orange, font=("Arial", 15, "bold"))
		X1 = Label(root2, text=x1, background=background, foreground=orange, font=("Arial", 15, "bold"))
		X2 = Label(root2, text=x2, background=background, foreground=orange, font=("Arial", 15, "bold"))
		label.pack()
		X1.pack()
		X2.pack()
	root2.mainloop()
title = Label(root, text="Quadratic Solver", background=background, foreground=orange, font=("Arial", 24, "bold"))

A = Entry(root, font=("Arial", 15, "bold"), justify="center", background=blue, foreground="White")
A_label = Label(root, text="Enter A Value", background=background, foreground=orange, font=("Arial", 15, "bold"))
B = Entry(root, font=("Arial", 15, "bold"), justify="center", background=blue, foreground="White")
B_label = Label(root, text="Enter B Value", background=background, foreground=orange, font=("Arial", 15, "bold"))
C = Entry(root, font=("Arial", 15, "bold"), justify="center", background=blue, foreground="White")
C_label = Label(root, text="Enter C Value", background=background, foreground=orange, font=("Arial", 15, "bold"))
button = Button(background=orange, foreground="White", text="Solve", width=5, font=("arial", 15, "bold"), command=Solve)

blank = Label(background=background)
blank1 = Label(background=background)
blank2 = Label(background=background)
blank3 = Label(background=background)
blank4 = Label(background=background)


title.pack()
blank.pack()
A_label.pack()
A.pack()
blank2.pack()
B_label.pack()
B.pack()
blank3.pack()
C_label.pack()
C.pack()
blank4.pack()
button.pack()

root.mainloop()
	
