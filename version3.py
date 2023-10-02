from tkinter import *
import random
from questions import questions
from pictures_list import list
import pictures_list

random_photo_1 = random.choice(list)
random_photo_2 = random.choice(list)


window = Tk()
window.title("Ποιος θα Ήθελες...")
window.config(padx=30, pady=30, bg="white")

canvas = Canvas(width=1200, height=800, bg="white", highlightthickness=0)


friend_photo_1 = PhotoImage(file=random_photo_1)
canvas.create_image(280, 350, image=friend_photo_1)
canvas.grid(row=0, column=0)
friend_photo_2 = PhotoImage(file=random_photo_2)
canvas.create_image(900, 350, image=friend_photo_2)
canvas.grid(row=0, column=2)



vs_logo = PhotoImage(file=r"/Users/dimitrioszaras/PycharmProjects/who_would_you/friend pics/vs.png")
canvas.create_image(600, 350, image=vs_logo)
canvas.grid(row=0, column=1)

button_exit = Button(window,  text="QUIT", bg="white", command=window.quit)
button_exit.grid()


window.mainloop()