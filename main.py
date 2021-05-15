from tkinter import *

BG_COLOR = '#756de7'

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20, bg=BG_COLOR)

canvas = Canvas(window, width=304, height=210, highlightthickness=0)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(152, 105, image=logo_image)
canvas.pack()

window.mainloop()
