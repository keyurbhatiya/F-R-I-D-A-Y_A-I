from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import time

def play_gif():
    root = Tk()
    root.geometry("1000x500")
    root.lift()
    root.attributes("-topmost", True)

    img = Image.open("giphy.gif")
    lbl = Label(root)
    lbl.place(x=0, y=0)

    iterator = ImageSequence.Iterator (img)

    for frame in ImageSequence.Iterator(img):
        frame = frame.resize((1000, 500))
        img_tk = ImageTk.PhotoImage(frame)
        lbl.config(image=img_tk)
        lbl.image = img_tk  # Keep a reference to avoid garbage collection issues
        root.update()
        time.sleep(0.05)
    root.destroy()




