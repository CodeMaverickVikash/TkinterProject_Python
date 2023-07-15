from tkinter import *
root=Tk()
root.geometry("655x335")
def getvals():
    print(f"The value of username is {uservalue.get()}")
    print(f"The value of password is {passvalue.get()}")

# Entry widget and Grid layout
user= Label(root, text="Username")
password= Label(root, text="Password")
user.grid()
password.grid(row=1)

# Variable classes in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar
uservalue= StringVar()
passvalue= StringVar()

Entry(root, textvariable=uservalue).grid(row=0, column=1)
Entry(root, textvariable=passvalue).grid(row=1, column=1)

Button(text="submit", command=getvals).grid()

root.mainloop()