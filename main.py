from tkinter import *
import pandas

ARABIC_FONT = ("Arial", 40, "italic")
ENGLISH_FONT = ("Arial", 60, "bold")
BACKGROUND_COLOR = "#B1DDC6"


windows = Tk()
windows.title(string="Flash Card App")
windows.config(background=BACKGROUND_COLOR)

# Create the card
canvas = Canvas(width=800, height=527, background=BACKGROUND_COLOR, highlightthickness=0)
title = canvas.create_text(400, 150, text='Arabic', font=ARABIC_FONT,)
word = canvas.create_text(400, 263, text='Test', font=ENGLISH_FONT,)

background_image = PhotoImage(file="./images/card_front.png")
canvas.create_image(403, 267, image=background_image)
title = canvas.create_text(400, 150, text='Arabic', font=ARABIC_FONT)
word = canvas.create_text(400, 300, text='test', font=ENGLISH_FONT)
canvas.grid(column=0, row=0, columnspan=2, padx=50, pady=50)

# Create the buttons

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, padx=150, bg=BACKGROUND_COLOR, highlightthickness=0)
wrong_button.grid(column=0, row=1, padx=100)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, padx=150, bg=BACKGROUND_COLOR, highlightthickness=0)
right_button.grid(column=1, row=1, padx=100)


windows.mainloop()