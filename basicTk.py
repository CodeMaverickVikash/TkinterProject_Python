from tkinter import *
from PIL import Image, ImageTk

window = Tk()

window.geometry("644x434")
window.title("MY GUI with Vikash")
window.minsize(300, 100)
# window.maxsize(1200, 700)

''' # important pack option/attributes
anchor= nw
side= left, right, top ,BOTTOM
fill= X, Y
padx
pady '''

# Handling text and images with Label widget
# title_label = Label(
#     text = '''this is wirtten for you. are you happy with me\n this is wirtten for you.are you happy with me \nthis is wirtten for you. are you happy with me''',
#     bg = "red",
#     fg = "white",
#     # padx = 2,
#     # pady = 2,
#     width = 100,
#     height = 100,
#     font = ("comicsansms", 19, "bold"),
#     # borderwidth = 3,
#     # relief = SUNKEN # border styling
# )
# title_label.pack(side=LEFT, fill= Y, padx=34, pady=34)

# handling images with tkinter GUI
# photo = PhotoImage(file="app_icon.png")
# varun_Label = Label(image=photo)
# varun_Label.pack()

# for jpg image
image= Image.open("./images/coding.jpeg")
photo= ImageTk.PhotoImage(image)
varun_Label= Label(image=photo)
varun_Label.pack(fill=BOTH, expand=TRUE)

# Button widget
# def clicked():
#     print('Button was clicked')

# button = Button(
#     text = "Button",
#     bg = 'red', fg = 'white',
#     # width = 5, height = 5
#     padx = 28, pady = 8,
#     # cursor = 'mouse',
#     command = clicked # Nothing but function
# )
# button.pack()

# Entry widget
# def getValues():
#     name = input.get()
#     print(name)

# input = Entry()
# input.pack()

# Button(text = 'Submit', command = getValues).pack()

# Text widget
# def getTextes():
#     print(textArea.get('1.0', END)) # add newline # "1.0" means that the input should be read from line one, character zero

# textArea = Text()
# textArea.pack()

# Button(text = 'Submit', command = getTextes).pack()

# Frame widget
# containerForWidget = Frame()
# containerForWidget.pack()



window.mainloop()