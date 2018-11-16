import socket
import _thread
import tkinter

serverPort=9999

serverSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientPairs=[]
CONFIRM="You are connected to the server, Please enter your username:"

serverSocket.bind(('',serverPort))

serverSocket.listen(2)

class ClientPair:
    def __init__(self,client1Address,client1Connect):
        self.client1Add=client1Address
        self.client1Connect = client1Connect
        self.client1Name=''
        self.client2Add=0
        self.client2Connect =''
        self.client2Name=''

    def addClient2(self,client2Address,client2Connect):
        self.client2Add=client2Address
        self.client2Connect=client2Connect

    def addUsernames(self,client1Username, client2Username):
        self.client1Name=client1Username
        self.client2Name=client2Username

    def toString(self):
        print(str(self.client1Add) + " and " + str(self.client2Add) + " are in conversation")

def chatHandler(clientPair):
    client1Con=clientPair.client1Connect
    client2Con=clientPair.client2Connect

    client1Con.send(("You are connected with "+clientPair.client2Name).encode())
    client2Con.send(("You are connected with "+clientPair.client1Name).encode())
    while True:
        _thread.start_new(clientHandler,(client1Con,client2Con,))
        _thread.start_new(clientHandler,(client2Con,client1Con))

def clientHandler(connection1,connection2):
    try:

        message = connection1.recv(1024).decode()
        connection2.send(message.encode())

    except ConnectionResetError:
        print("Someone is unreachable")


def main():
    print('Server is waiting for clients...')

    box=tkinter.Tk()
    box.mainloop()
    while True:
        connection1,address1=serverSocket.accept()

        connection1.send(CONFIRM.encode())
        print(address1+" has connected")
        clientPairN=ClientPair(address1,connection1)

        connection2,address2=serverSocket.accept()

        connection2.send(CONFIRM.encode())
        print(address2+" has connected")
        clientPairN.addClient2(address2,connection2)

        username1=connection1.recv(1024).decode()
        username2=connection2.recv(1024).decode()
        clientPairN.addUsernames(username1,username2)

        clientPairs.append(clientPairN)
        _thread.start_new(chatHandler,(clientPairN,))
        print(clientPairN.toString())


main()