import socket  # for socket
import threading
from time import sleep
from tkinter import *
import sys
import queue


'''
Client socket will run on a thread, GUI will run on another
'''

class Client:
    def __init__(self, username):
        self.username = username
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host):
        self.sock.connect(host)
        self.sock.send(self.username.encode())

    def send(self, data):
        self.sock.send(f'{self.username}: {data}'.encode())

    def close(self):
        self.sock.close()

    def receive(self, size):
        return self.sock.recv(size).decode()


root = Tk()
root.geometry('425x500')
root.title("CHATROOM")
root.resizable(width=True, height=True)

msg_list = []

client = Client("Client 1")
client.connect(('localhost', 5005))

frameTop = Text(root, bg="#ABB2B9")
frameTop.pack(side=TOP, padx=20, pady=20)

labelBottom = Label(root, bg="#ABB2B9")
labelBottom.place(relheight=1)

send_entry = Entry(root)
send_entry.pack()

scrollb = Scrollbar(frameTop)
scrollb.place(relheight=1, relx=0.974)
scrollb.config(command=frameTop.yview)

# frameTop.config(state=DISABLED)


def send_msg():
    temp = send_entry.get()
    client.send(temp)
    send_entry.delete(0, END)
    frameTop.insert(END, msg_list.pop(0))


send_button = Button(root, text="Send", command=send_msg)
send_button.pack(side=RIGHT)


def add():
    '''Add new message to the frame'''
    norm = Label(frameTop, text="hello\n\n", font='courier')
    norm.pack()


def main():
    while True:
        root.update()
        tempo = client.receive(1024)
        msg_list.append(tempo)

if __name__ == "__main__":
    try:
        main()
    except Exception:
        print("APP CLOSED")
