from tkinter import *
from tkinter import messagebox
import random
from questions import questions
from pictures_list import list

RED = "#e7305b"
WHITE = "#FFFFFF"
FONT_NAME = "Arial"

#path = r"/Users/dimitrioszaras/PycharmProjects/who_would_you/friend pics/"

random_question = random.choice(questions)
random_photo_1 = random.choice(list)
random_photo_2 = random.choice(list)

window = Tk()
window.title("Ποιος θα Ήθελες...")
window.config(padx=100, pady=50, bg=WHITE)

canvas = Canvas(width=1200, height=1200, bg=WHITE, highlightthickness=0)



#RANDOM QUESTION
title = Label(text=random_question, font=(FONT_NAME, 24, "bold"), fg=RED, background=WHITE)
title.grid(row=0, column=1)

#PHOTO IMAGE

friend_photo_1 = PhotoImage(file=random_photo_1) #this worκs for one photo
canvas.create_image(100, 200, image=friend_photo_1)
canvas.grid(row=3, column=0)

friend_photo_2 = PhotoImage(file=random_photo_2) #this worκs for one photo
canvas.create_image(400, 200, image=friend_photo_2)
canvas.grid(row=3, column=3)




#entry
input = Entry(width=20, highlightbackground=WHITE)
input.focus()
input.grid(row=1, column=1)


def ok_click():
    user_answer = input.get()
    if len(user_answer) == 0:
        messagebox.showinfo(title="Ωχ!", message="Γράψε ποιος ή ποιον θα ήθελες")
    else:
        is_ok = messagebox.askokcancel(title="ΠΡΟΣΟΧΗ", message=f"Είσαι σίγουρος για τον {user_answer};")

        if is_ok:
            input.delete(0, END)




#BUTTON
button = Button(text="OK", background=WHITE, highlightbackground=WHITE, command=ok_click)
button.grid(row=2, column=1)


window.mainloop()