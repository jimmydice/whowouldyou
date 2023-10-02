from tkinter import *
from PIL import ImageTk, Image
import random
from pictures_list import list


root = Tk()
root.title("Ποιος θα ήθελες να είσαι;")
root.config(padx=30, pady=30)

next_img = ImageTk.PhotoImage(Image.open(r"/Users/dimitrioszaras/PycharmProjects/who_would_you/friend pics/next.png"))

button_quit = Button(root, image=next_img, background="red", text="NEXT", command=root.quit)
button_quit.grid(row=1, column=1)

vs_logo = ImageTk.PhotoImage(Image.open(r"/Users/dimitrioszaras/PycharmProjects/who_would_you/friend pics/vs.png"))
vs_label = Label(image=vs_logo)
vs_label.grid(row=0, column=1)


while True:
    random_friends = random.sample(list, 2)
    image_1 = ImageTk.PhotoImage(Image.open(random_friends[0]))
    image_2 = ImageTk.PhotoImage(Image.open(random_friends[1]))

    my_label_1 = Label(image=image_1)
    my_label_1.grid(row=0, column=0)
    my_label_2 = Label(image=image_2)
    my_label_2.grid(row=0, column=2)

    root.mainloop()


