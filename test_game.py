from tkinter import *
from tkinter import messagebox
import random
from questions import questions
from pictures_list import list
import pictures_list

RED = "#e7305b"
WHITE = "#FFFFFF"
FONT_NAME = "Arial"

#path = r"/Users/dimitrioszaras/PycharmProjects/who_would_you/friend pics/"

#RANDOM_PHOTO = random.choice(list)

random_question = random.choice(questions)
random_photo_1 = random.choice(list)
random_photo_2 = random.choice(list)



window = Tk()
window.title("Ποιος θα Ήθελες...")
window.config(padx=50, pady=50, bg=WHITE)

background = PhotoImage(file=r"/Users/dimitrioszaras/PycharmProjects/who_would_you/friend pics/vs background.png")
vs_logo = PhotoImage(file=r"/Users/dimitrioszaras/PycharmProjects/who_would_you/friend pics/vs.png")
canvas = Canvas(width=1200, height=900)
#canvas.create_image(600, 600, image_number=vs_logo)
#canvas.grid(row=1, column=1)


#canvas.create_image(600, 380, image_number=vs_logo)
#canvas.create_text(620, 60, text=random_question, font=("Ariel", 30, "bold"))  #620, 60
#canvas.config(bg="white", highlightthickness=0)
#canvas.grid(row=0, column=0)




left = PhotoImage(file=random_photo_1)
left_choice = Button(image=left, highlightthickness=0, command=next)
left_choice.grid(row=1, column=0)
right = PhotoImage(file=random_photo_2)
right_choice = Button(image=right, highlightthickness=0, command=next)
right_choice.grid(row=1, column=2)




window.mainloop()