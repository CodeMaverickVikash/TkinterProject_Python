from tkinter import *

window=Tk()
window.title("Travel form")

def getvals():
    print("Submitting Form")
    print(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmodevalue.get(), foodservicevalue.get()}")
    with open("records.txt", "a") as f:
        f.write(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmodevalue.get(), foodservicevalue.get()}\n")

window.geometry("655x345")
Label(window, text="Welcome to vikash travel", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)

# text for our form
Label(window, text="Name").grid(row=1, column=2)
Label(window, text="Phone").grid(row=2, column=2)
Label(window, text="Gender").grid(row=3, column=2)
Label(window, text="Emergency Contact").grid(row=4, column=2)
Label(window, text="Payment mode").grid(row=5, column=2)

# tkinter variables for storing our entries
namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
paymentmodevalue=StringVar()
foodservicevalue=IntVar()

# entries for our form
Entry(window, textvariable=namevalue).grid(row=1, column=3)
Entry(window, textvariable=phonevalue).grid(row=2, column=3)
Entry(window, textvariable=gendervalue).grid(row=3, column=3)
Entry(window, textvariable=emergencyvalue).grid(row=4, column=3)
Entry(window, textvariable=paymentmodevalue).grid(row=5, column=3)

# checkbox & packing it
foodservice=Checkbutton(text="Want to prebook your meals?", variable=foodservicevalue)
foodservice.grid(row=6, column=3)

# button and packing it and assigning it a command
Button(text="Submit to vikash travels", command=getvals).grid(row=7, column=3)

window.mainloop()