import socket  # for socket
import threading
from time import sleep
from tkinter import *
import sys


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




frameTop = Frame(root, highlightbackground="blue", highlightthickness=2)
frameTop.pack(side=TOP, padx=20, pady=20)

frameBottom = Frame(root)
frameBottom.pack(side=BOTTOM)

send_entry = Entry(frameBottom)
send_entry.pack()


def send_msg():
    temp = send_entry.get()
    send_entry.delete(0, END)



send_button = Button(frameBottom, text="Send", command=send_msg)
send_button.pack(side=RIGHT)


def add():
    '''Add new message to the frame'''
    norm = Label(frameTop, text="hello", font='courier')
    norm.pack()


def client_1():
    try:
        client = Client("Client 1")
        client.connect(('localhost', 5005))
    except Exception:
        print("PROBLEM CONNECTING TO THE SERVER... TRY AGAIN LATER")
        sys.exit()


x = threading.Thread(target=client_1)


def main():
    x.start()

    while True:
        root.update()

if __name__ == "__main__":
    main()
