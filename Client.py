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
            msg = sockobj.recv(1024).decode()
            log.insert(tkinter.END, msg)
        except:
            log.insert(tkinter.END, 'User may have left the chat')
            break


def sendMessage(Entry = None):
    global message
    message = client_message.get()
    client_message.set("")  # Clears input field.
    if log.size() == 1:
        sockobj.send(message.encode())
        global username
        username = message
        log.insert(tkinter.END, 'Welcome ' + username + ' to the chat!')
        
    
    else:
        message = username + ': ' + message
        sockobj.send(message.encode())
        log.insert(tkinter.END, message)
        print(message)
        
        if message == "*quit*":
            sockobj.close()
            master.quit()

def closeWindow(Entry = None):
    client_message.set("*quit*")
    sendMessage()
    master.destroy()

#chat message
client_message = tkinter.StringVar()
client_message.set("Type in your username first.")

#shows past messages
scrollbar = tkinter.Scrollbar(frame)
log = tkinter.Listbox(frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
log.insert(tkinter.END, 'You can type in *quit* to end the chat. Press esc to close the window.')

# list of messages sent and received
log.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
log.pack()
frame.pack()


#chat entry
entry = tkinter.Entry(master, width = 50, textvariable=client_message)
entry.bind("<Return>", sendMessage())
entry.pack(side = tkinter.LEFT)

#send button
send_button = tkinter.Button(master, text="Send", command=sendMessage())
send_button.pack(side = tkinter.TOP)

master.protocol("WM_DELETE_WINDOW", closeWindow())
master.bind('<Escape>', lambda e: master.destroy())

master.mainloop()