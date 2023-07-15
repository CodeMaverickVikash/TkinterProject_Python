from tkinter import *
root=Tk()
def harry(event):
    print(f"you clicked me {event.x}, {event.y}")
root.geometry("644x334")

widget=Button(root, text="click me please")
widget.pack()

widget.bind('<Button-1>', harry)
widget.bind('<Double-1>', quit)

root.mainloop()