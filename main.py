from tkinter import *
import pandas
import random

ARABIC_FONT = ("Arial", 40, "italic")
ENGLISH_FONT = ("Arial", 60, "bold")
BACKGROUND_COLOR = "#B1DDC6"
FIRST_LANGUAGE = "French"
SECOND_LANGUAGE = "English"
CURRENT_WORD = {}
CARD_FRONT_COLOR = "Black"
CARD_BACK_COLOR = "white"
TIME_BETWEEN_FLIPPING_CARDS = 3000  # (milli second)

# Reading the data for the words file
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")

english_arabic_words = data.to_dict(orient="records")
print(data)
print(english_arabic_words)


# generating a new random word from the data.csv file
def next_word():
    global CURRENT_WORD, FLIP_TIMER
    windows.after_cancel(FLIP_TIMER)

    CURRENT_WORD = random.choice(english_arabic_words)
    current_word_in_english = CURRENT_WORD[FIRST_LANGUAGE]
    print(CURRENT_WORD)
    print(english_arabic_words.index(CURRENT_WORD))
    print(len(english_arabic_words))

    canvas.itemconfig(canvas_image, image=front_image_card)
    canvas.itemconfig(title, text=FIRST_LANGUAGE, fill=CARD_FRONT_COLOR)
    canvas.itemconfig(word, text=current_word_in_english, fill=CARD_FRONT_COLOR)
    FLIP_TIMER = windows.after(ms=TIME_BETWEEN_FLIPPING_CARDS, func=flip_card)


# flip the image from the card and show the translation of the current word
def flip_card():
    global FLIP_TIMER
    canvas.itemconfig(canvas_image, image=back_image_card)
    canvas.itemconfig(title, text=SECOND_LANGUAGE, fill=CARD_BACK_COLOR)
    canvas.itemconfig(word, text=CURRENT_WORD[SECOND_LANGUAGE], fill=CARD_BACK_COLOR)


def known_word():
    global data
    # index_current_word = english_arabic_words.index(CURRENT_WORD)
    # # data = data.drop(index_current_word)
    # print(data[FIRST_LANGUAGE] == CURRENT_WORD[FIRST_LANGUAGE].index())
    # print(data)
    # data.to_csv(path_or_buf="./data/words_to_learn.csv", index=False)
    english_arabic_words.remove(CURRENT_WORD)
    words_to_learn = pandas.DataFrame(english_arabic_words)
    words_to_learn.to_csv(path_or_buf="./data/words_to_learn.csv", index=False)
    # print(words_to_learn)
    next_word()


windows = Tk()
windows.title(string="Flash Card App")
windows.config(background=BACKGROUND_COLOR, padx=50, pady=50)

FLIP_TIMER = windows.after(ms=3000, func=next_word)

# Create the card
canvas = Canvas(width=800, height=527, background=BACKGROUND_COLOR, highlightthickness=0)
title = canvas.create_text(400, 150, text='Arabic', font=ARABIC_FONT, )
word = canvas.create_text(400, 263, text='Test', font=ENGLISH_FONT, )
back_image_card = PhotoImage(file="./images/card_back.png")
front_image_card = PhotoImage(file="./images/card_front.png")
canvas_image = canvas.create_image(403, 267, image=front_image_card)
title = canvas.create_text(400, 150, text='Arabic', font=ARABIC_FONT)
word = canvas.create_text(400, 300, text='test', font=ENGLISH_FONT)
canvas.grid(column=0, row=0, columnspan=2)

# Create the buttons

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_word)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=known_word)
right_button.grid(column=1, row=1)

next_word()

windows.mainloop()
