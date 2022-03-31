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
clients = []
messages = queue.Queue()
sock.bind(('10.3.9.39', 5005))
sock.listen()
print("Server is listening...")


def waiting():
    while True:
        print("Checking for new connection...")
        conn, address = sock.accept() # New Connection
        clients.append(conn)
        if conn not in readable:
            readable.append(conn)
        for i in clients:
            i.send(f"Welcome {i}".encode())


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
            for i in clients:
                i.send(messages.get().encode())
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
