# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 09:50:11 2018

@author: hillg2
"""

import socket
serverHost = 'localHost'
serverPort = 9999

sockobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockobj.connect((serverHost, serverPort))

message = input()

for line in message :
    print('User 1: ', message)
    sockobj.send(line.encode())
    data = sockobj.recv(1024).decode()
    print('User 2: ', str(data))

sockobj.close()