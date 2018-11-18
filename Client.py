# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 09:50:11 2018

@author: hillg2
"""
import socket
import tkinter

serverHost = 'localhost'
serverPort = 9999

sockobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockobj.connect((serverHost, serverPort))

master = tkinter.Tk()

frame = tkinter.Frame(master)

def receive():
    while True:
        try:
            msg = sockobj.recv(2048).decode()
            log.insert(tkinter.END, msg)
        except:
            log.insert(tkinter.END, 'User may have left the chat')
            break


def send(Entry = None):
    message = client_message.get()
    client_message.set("")  # Clears input field.
    if log.size() == 2:
        sockobj.send(message.encode())
        username = message
        log.insert(tkinter.END, 'Welcome ' + username + ' to the chat!')
        
    
    else:
        sockobj.send(message.encode())
        log.insert(tkinter.END, message)
        print(message)
        
        if message == "*quit*":
            sockobj.close()
            master.quit()
        

def close(Entry = None):
    client_message.set("*quit*")
    send()

#chat message
client_message = tkinter.StringVar()
client_message.set("Type your messages here.")

#shows past messages
scrollbar = tkinter.Scrollbar(frame)
log = tkinter.Listbox(frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
log.insert(tkinter.END, 'Please type in a username.')
log.insert(tkinter.END, 'You can type in *quit* to end the chat.')

# list of messages sent and received
log.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
log.pack()
frame.pack()

username = ''

#chat entry
entry = tkinter.Entry(master, textvariable=client_message)
entry.bind("<Return>", send)
entry.pack(side = tkinter.LEFT)

#send button
send_button = tkinter.Button(master, text="Send", command=send)
send_button.pack(side = tkinter.TOP)

master.protocol("WM_DELETE_WINDOW", close)

master.mainloop()