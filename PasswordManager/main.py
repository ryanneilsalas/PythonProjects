from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox

FONT = ("Arial", 10, "bold")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
           'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    password_input.delete(0, END)

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_number
    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website = website_input.get()
    user = user_input.get()
    password = password_input.get()

    if website == "" or user == "":
        messagebox.showwarning(title="Empty User or Password", message="Please add User/Email or Password!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Save? email/user:{user} password:{password}")
        if is_ok:
            with open(f"data.txt", mode="a") as completed_password:
                saved_pass = f"{website}|{user}|{password}\n"
                completed_password.write(saved_pass)

    website_input.delete(0, END)
    password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("My Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(column=1, row=0)
lbl_website = Label(text="Website:", font=FONT)
lbl_website.grid(column=0, row=2)
lbl_user = Label(text="Email/Username:", font=FONT)
lbl_user.grid(column=0, row=3)
lbl_pass = Label(text="Password:", font=FONT)
lbl_pass.grid(column=0, row=4)

website_input = Entry(width=39)
website_input.grid(column=1, row=2, columnspan=2)
website_input.focus()
user_input = Entry(width=39)
user_input.grid(column=1, row=3, columnspan=2)
user_input.insert(0, "ryanneilsalas@gmail.com")
password_input = Entry(width=27)
password_input.grid(column=1, row=4, sticky="e")

btn_generate = Button(text="Generate Password", command=generate_pass)
btn_generate.grid(column=2, row=4)
btn_save = Button(text="Save", width=33, command=save_pass)
btn_save.grid(column=1, row=5, columnspan=2)
window.mainloop()
