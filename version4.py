from tkinter import *
import random
from ready_templates import list
from questions import questions


random_photo = random.choice(list)
random_question = random.choice(questions)
BACKGROUND_COLOR = "white"

window = Tk()
window.title("Ποιος θα ήθελες")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

vs_photo = PhotoImage(file=random_photo)


def next_card():
    global random_photo, vs_photo
    random_question = random.choice(questions)
    canvas.itemconfig(card_question, text=random_question)
    canvas.itemconfig(card_background, image=vs_photo)



canvas = Canvas(width=800, height=400)
card_background = canvas.create_image(400, 263, image=vs_photo)
card_question = canvas.create_text(400, 30, text=random_question, font=("Ariel", 20))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


tick_image = PhotoImage(file="images/tick png.png")
left_button = Button(image=tick_image, highlightthickness=0, command=next_card)
left_button.grid(row=1, column=0)


right_button = Button(image=tick_image, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()