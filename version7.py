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



def update_pics():
    selected_pics = []
    while len(selected_pics) < 2:
        pic = ImageTk.PhotoImage(Image.open(random.choice(list)))
        if pic not in selected_pics:
            selected_pics.append(pic)

    labels = []
    for i, pic in enumerate(selected_pics):
        pic_path = pic[1]
        image = Image.open(pic_path)
        photo = ImageTk.PhotoImage(image)
        my_label_1 = Label(image=pic_path])
        my_label_1.grid(row=0, column=0)
        my_label_2 = Label(image=pi)
        my_label_2.grid(row=0, column=2)



update_pics()


root.mainloop()


