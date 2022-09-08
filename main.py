from tkinter import *
import pandas
import random

ARABIC_FONT = ("Arial", 40, "italic")
ENGLISH_FONT = ("Arial", 60, "bold")
BACKGROUND_COLOR = "#B1DDC6"
FIRST_LANGUAGE = "English"
SECOND_LANGUAGE = "Arabic"
TRANSLATION = ""
CARD_FRONT_COLOR = "Black"
CARD_BACK_COLOR= "white"
NEXT_IMAGE = ""


windows = Tk()
windows.title(string="Flash Card App")
windows.config(background=BACKGROUND_COLOR, padx=50, pady=50)


# Reading the data for the words file
data = pandas.read_csv("./data/English Arabic - Sheet2.csv")
english_words = data.to_dict(orient="records")
print(english_words)


# generating a new random word from the data.csv file
def next_word():
    global TRANSLATION, NEXT_IMAGE
    if NEXT_IMAGE != "":
        windows.after_cancel(NEXT_IMAGE)
        # windows.after_cancel(flip_image)

    random_word = random.choice(english_words)
    random_word_in_english= random_word[FIRST_LANGUAGE]
    random_word_in_arabic = random_word[SECOND_LANGUAGE]
    print(random_word)
    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(title, text=FIRST_LANGUAGE, fill=CARD_FRONT_COLOR)
    canvas.itemconfig(word, text=random_word_in_english, fill=CARD_FRONT_COLOR)
    TRANSLATION = random_word_in_arabic
    NEXT_IMAGE = windows.after(ms=3000, func=flip_card)


# flip the image from the card and show the translation of the current word
def flip_card():
    global NEXT_IMAGE
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(title, text=SECOND_LANGUAGE, fill=CARD_BACK_COLOR)
    canvas.itemconfig(word, text=TRANSLATION, fill=CARD_BACK_COLOR)
    NEXT_IMAGE = windows.after(ms=3000, func=next_word)


# Create the card
canvas = Canvas(width=800, height=527, background=BACKGROUND_COLOR, highlightthickness=0)
title = canvas.create_text(400, 150, text='Arabic', font=ARABIC_FONT,)
word = canvas.create_text(400, 263, text='Test', font=ENGLISH_FONT,)
back_image = PhotoImage(file="./images/card_back.png")
front_image = PhotoImage(file="./images/card_front.png")
canvas_image = canvas.create_image(403, 267, image=front_image)
title = canvas.create_text(400, 150, text='Arabic', font=ARABIC_FONT)
word = canvas.create_text(400, 300, text='test', font=ENGLISH_FONT)
canvas.grid(column=0, row=0, columnspan=2)

# Create the buttons

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_word)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_word)
right_button.grid(column=1, row=1)

next_word()


windows.mainloop()