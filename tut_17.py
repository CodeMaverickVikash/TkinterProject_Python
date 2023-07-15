from tkinter import *

window = Tk()
window.geometry("755x545")

def myfunc():
    print("my best for you")
def help():
    print("i will help you")
    a=tmsg.showinfo("Help", "Harry will help you with this gui")
def rate():
    print("rate us")
    value=tmsg.askquestion("Was your experience Good?", "How was your experience")
    print(value)
    if value=="yes":
        msg= "Great. Rate us on appstore please"
    else:
        msg= "Tell us what went wrong. we will call you soon"
    tmsg.showinfo("Experience", msg)
def Divya():
    ans=tmsg.askretrycancel("Divya se dosti ker lo", "Sorry Divya nhi banegi apki dost")
    if ans:
        print("Retry karne per bhi kuch nhi hoga")
    else:
        print("Bahot badiya bhai cancel ker diya warna bahot pitte")

# menu and submenu in tkinter
# use these to cearte a non dropdown menu
# mymenu=Menu(window)
# mymenu.add_command(label="File", command=myfunc)
# mymenu.add_command(label="Exit", command=quit)
# window.config(menu=mymenu)

# create a menubar
mainmenu = Menu(window)

# Menu
m1 = Menu(mainmenu, tearoff=0) # To remove the dashed line
m1.add_command(label="New project", command=myfunc)
m1.add_command(label="Save", command=myfunc)

m1.add_separator()

m1.add_command(label="Save as", command=myfunc)
m1.add_command(label="Print", command=myfunc)
window.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)

m2= Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut", command=myfunc)
m2.add_command(label="Copy", command=myfunc)
m2.add_separator()
m2.add_command(label="Paste", command=myfunc)
m2.add_command(label="Find", command=myfunc)
window.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit", menu=m2)

# messagebox in tkinter
import tkinter.messagebox as tmsg

m3= Menu(mainmenu, tearoff=0)
m3.add_command(label="Help", command=help)
m3.add_command(label="Rate us", command=rate)
m3.add_command(label="Befriend Diviya", command=Divya)
mainmenu.add_cascade(label="Help", menu=m3)
window.config(menu=mainmenu)

window.mainloop()