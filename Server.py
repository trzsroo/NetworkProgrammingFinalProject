import socket

serverPort = 9999

serverSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

serverSocket.bind(('',serverPort))


