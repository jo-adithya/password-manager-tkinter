from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_entry():
    website = web_input.get()
    email = email_input.get()
    password = pass_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title='Empty username or password',
                               message='Please make sure you did not leave any fields empty.')
        return

    is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered:\n'
                                                  f'Email: {email}\n'
                                                  f'Password: {password}\n'
                                                  f'Is it okay to save?')
    if is_ok:
        with open('password.txt', mode='a+') as f:
            f.write(f'{website} | {email} | {password}\n')
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
