import json
import os
from tkinter import *
from tkinter import  messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def pass_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letter=[random.choice(letters) for _ in range(nr_letters)]
    symbol=[random.choice(symbols) for _ in range(nr_symbols)]
    number=[random.choice(numbers) for _ in range(nr_numbers)]
    password_list=letter+symbol+number

    random.shuffle(password_list)

    password ="".join(password_list)

    entry_password.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=entry_website.get()
    email=entry_email.get()
    password=entry_password.get()
    current_dir = os.path.dirname(__file__)
    image_path = os.path.join(current_dir, "data.json")

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:    
            data_file=open(image_path, "r")
            data=json.load(data_file )
            data.update({website:{"email":email,"password":password}})
        except FileNotFoundError:
            data_file=open(image_path, "w")
            data={website:{"email":email,"password":password}}
        data_file=open(image_path, "w")
        json.dump(data, data_file, indent=4)
        entry_website.delete(0, END)
        entry_password.delete(0,END)
        entry_website.focus()

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
        website=entry_website.get()
        current_dir = os.path.dirname(__file__)
        image_path = os.path.join(current_dir, "data.json")
        try:
             data_file=open(image_path,"r")
             data=json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found.")
        else:
            if website in data:
                email=data[website]["email"]
                password=data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            elif website not in data:
                messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

        
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas=Canvas(width=200, height=200)
current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "logo.png")
locker_img = PhotoImage(file=image_path)
canvas.create_image(100, 100, image=locker_img)
canvas.grid(row=0, column=1)

website_label=Label(text="Website:")
website_label.grid(row=1, column=0)
email_label=Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label=Label(text="Password:")
password_label.grid(row=3, column=0)

entry_website=Entry(width=36)
entry_website.grid(row=1, column=1, columnspan=2)
entry_website.focus()
entry_email=Entry(width=36)
entry_email.grid(row=2, column=1, columnspan=2)
entry_email.insert(0, "harshith@gmail.com")
entry_password=Entry(width=36)
entry_password.grid(row=3, column=1, columnspan=2)

generate_password_button=Button(text="Generate Password",command=pass_gen)
generate_password_button.grid(row=3, column=2)
add_button=Button(text="Add", width=36,command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button=Button(text="Search", width=13, command=search_password)
search_button.grid(row=1, column=2)






window.mainloop()