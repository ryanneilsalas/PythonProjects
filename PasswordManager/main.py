from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import json

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
    new_data = {
        website: {
            "email": user,
            "password": password,
        }
    }
    if website == "" or user == "":
        messagebox.showwarning(title="Empty User or Password", message="Please add User/Email or Password!")
    else:
        try:
            with open(f"data.json", mode="r") as completed_password:
                # reading old data
                data = json.load(completed_password)

        except FileNotFoundError:
            with open(f"data.json", mode="w") as completed_password:
                json.dump(new_data, completed_password, indent=4)
        else:
            # updating old data
            data.update(new_data)

            with open("data.json", "w") as completed_password:
                # saving updated data
                json.dump(data, completed_password, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


def search_password():
    website = website_input.get()
    try:
        with open(f"data.json", mode="r") as completed_password:
            data = json.load(completed_password)
            user_email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"User/Email: {user_email}\n Password: {password}")
    except FileNotFoundError:
        messagebox.showwarning(title="Warning", message="You have not created any password yet")
    except KeyError:
        messagebox.showwarning(title="Warning", message=f"{website} data not found")


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

website_input = Entry(width=27)
website_input.grid(column=1, row=2, sticky="e", padx=10)
website_input.focus()
user_input = Entry(width=42)
user_input.grid(column=1, row=3, columnspan=2)
user_input.insert(0, "ryanneilsalas@gmail.com")
password_input = Entry(width=27)
password_input.grid(column=1, row=4, sticky="e", padx=10)

btn_generate = Button(text="Generate", width=14, command=generate_pass)
btn_generate.grid(column=2, row=4)
btn_save = Button(text="Save", width=20, command=save_pass)
btn_save.grid(column=1, row=5, columnspan=2, pady=10)
btn_search = Button(text="Search", width=14, command=search_password)
btn_search.grid(column=2, row=2, )
window.mainloop()
