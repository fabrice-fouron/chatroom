import threading
import socket
import queue
from time import sleep
from tkinter import Tk, Message


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connected = [sock]
tosend = []
info = {}
readable = []
messages = queue.Queue()
sock.bind(('localhost', 5005))
sock.listen()
print("Server is listening...")

def waiting():
    while True:
        print("Checking for new connection...")
        conn, address = sock.accept() # New Connection
        if conn not in readable:
            readable.append(conn)
            print(f"Welcome {conn.recv(1024).decode()}")


def message_handling():
    while True:
        sleep(1)
        print("Handling messages")
        for i in readable:
            temp = i.recv(1024).decode()
            messages.put(temp)

def print_out():
    while True:
        if not messages.empty:
            print(messages.get())
        sleep(1)

x = threading.Thread(target=waiting)
y = threading.Thread(target=message_handling)
z = threading.Thread(target=print_out)

x.start()
y.start()
z.start()


# root = Tk()
# root.geometry('425x500')
# root.title("CHATROOM")

# def new_message(client, content):
#     texts = client + ": " + content
#     message = Message(master=root, justify='left', text=texts, fg="blue", width=400)
#     message.pack()


# root.mainloop()