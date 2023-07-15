from tkinter import *

root = Tk()

root.geometry("655x333")

# Frame widget
f1 = Frame(root, bg="green", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill="y")

f2 = Frame(root, borderwidth=8, bg="grey", relief=SUNKEN)
f2.pack(side=TOP, fill="x")

# Label widget
l = Label(f1, text="Project Tkinter - Pycharm")
l.pack(pady=142)

l = Label(f2, text="Wellcome to pubg world", font="Helvetica 16 bold", fg="red", pady=22)
l.pack()

root.mainloop()