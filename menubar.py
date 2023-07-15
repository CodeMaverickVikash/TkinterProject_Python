from tkinter import *

root=Tk()
root.title("vikash")
root.geometry("450x547")

def newfile():
    pass

# use these to create non dropdown menu
# mymenu= Menu(root)
# mymenu.add_command(label="File", command=newfile)
# mymenu.add_command(label="Exit", command=quit)
# root.config(menu=mymenu)

# use these to create dropdown menu
filemenu = Menu(root)
submenu= Menu(filemenu)
submenu.add_command(label="New")
submenu.add_command(label="save")
submenu.add_command(label="print")

filemenu.add_cascade(label="File", menu=submenu)

# Display menu
root.config(menu=filemenu)

root.mainloop()