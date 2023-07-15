from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.title("Slider tutorial")
root.geometry("645x544")

def getdollar():
    print(f"We have credited {myslider2.get()} dollor to your bank account")
    tmsg.showinfo("Amount credited", f"We have credited {myslider2.get()} dollor to your bank account")
def order():
    tmsg.showinfo("Order received", f"We have received your order {var.get()}. thanks for ordering")

# myslider= Scale(root, from_=0, to=100)
# myslider.pack()

Label(root, text="How many dollars do you want?").pack()

myslider2= Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=50)
# myslider2.set(34)
myslider2.pack()
Button(root, text="Get dollars!", pady=10, command=getdollar).pack()

# Radiobutton tutorial
# var=IntVar()
var=StringVar()
var.set("Radio")
# var.set(1)
Label(root, text="What would you like to have sir", justify=LEFT, padx=14, font="lucida 19 bold").pack()

radio=Radiobutton(root, text="Dosa", padx=14, variable=var, value="Dosa").pack(anchor="w")
radio=Radiobutton(root, text="Idly", padx=14, variable=var, value="Idly").pack(anchor="w")
radio=Radiobutton(root, text="Paratha", padx=14, variable=var, value="Paratha").pack(anchor="w")
radio=Radiobutton(root, text="Samosa", padx=14, variable=var, value="Samosa").pack(anchor="w")
# ritrieve value of radiobutton
Button(text="Order now", command=order).pack()

root.mainloop()