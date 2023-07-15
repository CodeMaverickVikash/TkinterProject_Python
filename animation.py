# from tkinter import *

# window = Tk()
# window.geometry('500x900')

# def run_animation():
#     pass

# gif = PhotoImage(file = './images/7LP8.gif')
# print(gif.n_f)
# Label(window, image = gif).place(x = 0, y = 0)

# Button(window, text = 'Run animation', bg = 'blue', fg = 'white', font = 30, command = run_animation).pack(pady = 50)

# window.mainloop()


# import tkinter as tk
# from PIL import Image

# root = tk.Tk()
# file="./images/7LP8.gif"

# info = Image.open(file)

# frames = info.n_frames  # gives total number of frames that gif contains

# # creating list of PhotoImage objects for each frames
# im = [tk.PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]

# count = 0
# anim = None
# def animation(count):
#     global anim
#     im2 = im[count]

#     gif_label.configure(image=im2)
#     count += 1
#     if count == frames:
#         count = 0
#     anim = root.after(50,lambda :animation(count))

# def stop_animation():
#     root.after_cancel(anim)

# gif_label = tk.Label(root,image="")
# gif_label.pack()

# start = tk.Button(root,text="start",command=lambda :animation(count))
# start.pack()

# stop = tk.Button(root,text="stop",command=stop_animation)
# stop.pack()

# root.mainloop()


import tkinter
from PIL import Image, ImageTk, ImageSequence

class App:
    def __init__(self, parent):
        self.parent = parent
        self.canvas = tkinter.Canvas(parent, width=1400, height=900)
        self.canvas.pack()
        self.sequence = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                                    Image.open(
                                    r'./images/7LP8.gif'))]
        self.image = self.canvas.create_image(200,200, image=self.sequence[0])
        self.animate(1)
    def animate(self, counter):
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        self.parent.after(20, lambda: self.animate((counter+1) % len(self.sequence)))

root = tkinter.Tk()
app = App(root)
root.mainloop()