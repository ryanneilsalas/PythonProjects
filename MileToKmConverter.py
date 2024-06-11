from tkinter import *


def button_clicked():
    calculate = float(text_input.get()) * 1.609
    lbl_convert.config(text=round(calculate, 2))


window = Tk()
window.title("Mile to Km Converter")
window.minsize(50, 100)
window.config(padx=20, pady=20)

text_input = Entry(width=10)
text_input.grid(column=1, row=0)
# Label
lbl_miles = Label(text="Miles", font=("Arial", 10))
lbl_miles.grid(column=2, row=0)
lbl_km = Label(text="Km", font=("Arial", 10))
lbl_km.grid(column=2, row=1)
lbl_equals = Label(text="is equal to", font=("Arial", 10))
lbl_equals.grid(column=0, row=1)
lbl_convert = Label(text="0", font=("Arial", 10))
lbl_convert.grid(column=1, row=1)
# button


button = Button(text="Convert", command=button_clicked)
button.grid(column=1, row=3, padx=10, pady=10)
window.mainloop()
