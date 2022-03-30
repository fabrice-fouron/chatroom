from tkinter import *
import time
import threading

root = Tk()
root.geometry('425x500')
root.title("CHATROOM")
root.resizable(width=True, height=True)
x = 0
y = 0

def add():
    norm = Label(frame, text="hello", font='courier')
    norm.pack()


frame = Frame(root, bg="#000000")
frame.pack()

while True:
    frame.update()
    add()
    y += 5
    time.sleep(1)
    print("updating")
