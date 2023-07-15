from tkinter import *
root=Tk()
root.geometry("655x534")

def update():
    print("Updating th Gui")
    root.geometry(f"{width.get()}x{height.get()}")

width= StringVar()
height= StringVar()

Entry(root, textvariable=width).pack()
Entry(root, textvariable=height).pack()

Button(root, text="Apply", command=update).pack()

root.mainloop()