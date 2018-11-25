# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 09:50:11 2018

@author: hillg2
"""
import socket
import tkinter
import threading

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
            if(log.size() > 2):
                log.itemconfig(log.size()-1, fg = 'green')
        except:
            log.insert(tkinter.END, 'User may have left the chat')
            break

def cutMessage(message):
    if(len(message) > 90):
        msg1 = message[:90]
        sockobj.send(msg1.encode())
        log.insert(tkinter.END, msg1)
        msg2 = message[90:]
        cutMessage(msg2)
    elif len(message < 90):
        sockobj.send(message.encode())
        log.insert(tkinter.END, message)

def sendMessage(Entry = None):
    global message
    message = client_message.get()
    client_message.set("")  # Clears input field.
    if log.size() == 2:
        sockobj.send(message.encode())
        global username
        username = message
        message = 'Welcome ' + username + ' to the chat!'
        log.insert(tkinter.END, message)
        
    
    else:
        if message == "*quit*":
            sockobj.send(message.encode())
            log.insert(tkinter.END, message)
            sockobj.close()
            master.quit()
        else:  
            message = username + ': ' + message
            if len(message) < 90 :
                sockobj.send(message.encode())
                log.insert(tkinter.END, message)
            else:
                cutMessage(message)
        

def closeWindow(Entry = None):
    client_message.set("*quit*")
    sendMessage()
    master.destroy()

#chat message
client_message = tkinter.StringVar()
client_message.set("Type in your username first.")

#shows past messages
scrollbar = tkinter.Scrollbar(frame)
log = tkinter.Listbox(frame, width=100, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
log.insert(tkinter.END, 'You can type in *quit* or press esc to close the window. \n')

scrollbar.config(command=log.yview)

# list of messages sent and received
log.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
log.pack()
frame.pack()

#chat entry
entry = tkinter.Entry(master, width = 100, textvariable=client_message)
entry.bind("<Return>", sendMessage)
entry.pack(side = tkinter.LEFT)

#send button
send_button = tkinter.Button(master, text="Send", command=sendMessage)
send_button.pack(side = tkinter.TOP)

master.protocol("WM_DELETE_WINDOW", closeWindow)
master.bind('<Escape>', lambda e: master.destroy())

rThread = threading.Thread(target = receive)
rThread.start()
master.mainloop()