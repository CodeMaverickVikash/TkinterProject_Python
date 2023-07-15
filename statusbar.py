from tkinter import *
root= Tk()
root.title("StatusBar")
root.geometry("655x534")

root.wm_iconbitmap("1.ico")
root.configure(background="red")
Button(text="Close", command=root.destroy).pack()

def upload():
    statusvar.set("Busy..")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready Now")

statusvar= StringVar()
statusvar.set("Ready")

sbar=Label(root, textvariable=statusvar, relief=SUNKEN, anchor="w")
sbar.pack(side=BOTTOM, fill=X)
Button(root, text="Upload", command=upload).pack()

root.mainloop()