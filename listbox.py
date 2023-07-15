from tkinter import *
root=Tk()
root.title("ListBox tutorial")
root.geometry("645x534")

i=0
def add():
    global i
    lbx.insert(ACTIVE, f"{i}")
    i+=1

lbx= Listbox(root)
lbx.pack()
lbx.insert(END, "First item of our listbox")

Button(root, text="Add item", command=add).pack()

# For connecting scrollbar to widget
# 1. widget(yscrollcommand=scrollbar.set)
# 2. scrollbar.config(command=widget.yveiw)

# scrollbar creating
scrollbar= Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# create widget and connecting to scrollbar
listbox= Listbox(root, yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
listbox.pack(fill="both", padx=22)

for i in range(34):
    listbox.insert(END, f"Item {i}")

'''text= Text(root, yscrollcommand=scrollbar.set)
scrollbar.config(command=text.yview)
text.pack(fill=BOTH)'''

root.mainloop()