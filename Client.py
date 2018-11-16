# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 09:50:11 2018

@author: hillg2
"""

import socket
import tkinter

serverHost = 'localHost'
serverPort = 9999

sockobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockobj.connect((serverHost, serverPort))

# taken = True
# while taken:
#     usernameButton = tkinter.Tk()
#     tkinter.Label(usernameButton, text='Username').grid(row=0)
#     e = tkinter.Entry(usernameButton)
#     e.grid(row=0, column=1)
#     tkinter.mainloop()
#
#     username = e.get()
#     sockobj.send(username.encode(),(serverHost, serverPort))
#
# chatScreen = tkinter.Tk()
# tkinter.Label(chatScreen, text='Send').grid(row=0)
# e1 = tkinter.Entry(chatScreen)
# e1.grid(row=10, column=1)
# tkinter.mainloop()
#
# username = e1.get()
# sockobj.send(chatScreen.encode(),(serverHost, serverPort))


print('Welcome to this chat room!')

message = input()
while True:
    for line in message :
        if message:
            print('You: ', message)
            sockobj.send(message.encode(), (serverHost, serverPort))
        else:
            otherMessage = sockobj.recv(2048).decode()
            print('Other User: ', str(otherMessage))

sockobj.close()