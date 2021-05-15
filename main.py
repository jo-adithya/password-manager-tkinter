from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

BG_COLOR = '#756de7'
FONT = ('Arial', 14, 'normal')
FONT_INPUT = ('Arial', 16, 'normal')
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    nr_letters= randint(8, 12)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(3, 6)

    password = [choice(letters) for _ in range(nr_letters)]
    password.extend([choice(symbols) for _ in range(nr_symbols)])
    password.extend([choice(numbers) for _ in range(nr_numbers)])

    shuffle(password)
    password = "".join(password)
    is_ok = messagebox.askokcancel(title='Password Generator', message=f'Password: {password}')
    if is_ok:
        pass_input.insert(0, password)
        pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_entry():
    website = web_input.get()
    entry = {
        website: {
            'email': email_input.get(),
            'password': pass_input.get(),
        }
    }

    if len(website) == 0 or len(entry[website]["email"]) == 0 or len(entry[website]["password"]) == 0:
        messagebox.showwarning(title='Empty username or password',
                               message='Please make sure you did not leave any fields empty.')
        return

    is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered:\n'
                                                  f'Email: {entry[website]["email"]}\n'
                                                  f'Password: {entry[website]["password"]}\n'
                                                  f'Is it okay to save?')
    if is_ok:
        try:
            with open('password.json', mode='r') as file:
                # Read existing data
                data = json.load(file)
        except (FileNotFoundError, JSONDecodeError):
            with open('password.json', mode='w') as file:
                json.dump(entry, file, indent=4)
        else:
            # Update existing data with new data
            data.update(entry)

            with open('password.json', mode='w') as file:
                # Save the updated data
                json.dump(data, file, indent=4)
        finally:
            web_input.delete(0, END)
            email_input.delete(0, END)
            pass_input.delete(0, END)
            web_input.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50, bg=BG_COLOR)

# Canvas
canvas = Canvas(window, width=220, height=210, highlightthickness=0)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(110, 105, image=logo_image)
canvas.grid(row=0, column=1)

# Labels
website = Label(text='Website:', font=FONT, pady=5, bg=BG_COLOR, fg='#fff')
email = Label(text='Email/Username:', font=FONT, pady=5, bg=BG_COLOR, fg='#fff')
password = Label(text='Password:', font=FONT, pady=5, bg=BG_COLOR, fg='#fff')
website.grid(row=1, column=0)
email.grid(row=2, column=0)
password.grid(row=3, column=0)

# Inputs
web_input = Entry(width=40, bg=BG_COLOR, highlightthickness=0, borderwidth=1, font=FONT_INPUT, fg='white')
email_input = Entry(width=40, bg=BG_COLOR, highlightthickness=0, borderwidth=1, font=FONT_INPUT, fg='white')
pass_input = Entry(width=24, bg=BG_COLOR, highlightthickness=0, borderwidth=1, font=FONT_INPUT, textvariable=password, show='●', fg='white')
web_input.focus()
web_input.grid(row=1, column=1, columnspan=2)
email_input.grid(row=2, column=1, columnspan=2)
# email_input.insert(0, 'your email')
pass_input.grid(row=3, column=1)

# Buttons
gen_pass = Button(text='Generate Password', highlightthickness=0, width=15, pady=2, bg='blue', borderwidth=0, fg=BG_COLOR, command=password_generator)
add_btn = Button(text='Add', highlightthickness=0, width=40, pady=2, bg='white', borderwidth=0, fg=BG_COLOR, command=add_entry)
gen_pass.grid(row=3, column=2)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
