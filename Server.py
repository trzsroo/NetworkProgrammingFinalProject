import socket
import _thread
import tkinter

serverPort=9999

serverSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientPairs=[]
CONFIRM="You are connected to the server, Please enter your username:"
MESSAGECONFIRM="..."

serverSocket.bind(('',serverPort))

serverSocket.listen(2)

#class to keep clients who are connected with each other together
class ClientPair:
    def __init__(self,client1Address,client1Connect):
        self.client1Add=client1Address
        self.client1Connect=client1Connect
        self.client1Name=''
        self.client2Add=0
        self.client2Connect=''
        self.client2Name=''

    def addClient2(self,client2Address,client2Connect):
        self.client2Add=client2Address
        self.client2Connect=client2Connect

    def addUsernames(self,client1Username,client2Username):
        self.client1Name=client1Username
        self.client2Name=client2Username

    def toString(self):
        print(str(self.client1Name)+" and "+str(self.client2Name)+" are in conversation")

#thread method for clients in chat, takes in a ClientPair object
def chatHandler(clientPair):
    client1Con=clientPair.client1Connect
    client2Con=clientPair.client2Connect

    try:
        client1Con.send(("You are connected with "+clientPair.client2Name).encode())
        client2Con.send(("You are connected with "+clientPair.client1Name).encode())
        while True:
            try:
                _thread.start_new(clientHandler,(client1Con,client2Con,))
                _thread.start_new(clientHandler,(client2Con,client1Con))
            except:
                break
    except ConnectionResetError:
        client1Con.send((clientPair.client2Name+" has disconnected").encode())
        client2Con.send((clientPair.client1Name+" has disconnected").encode())

#thread method for each client conversation, receives message from one client and immediately sends
#message to other client
def clientHandler(connection1,connection2):
    message=connection1.recv(1024).decode()
    print(message)
    #connection1.send(MESSAGECONFIRM.encode())
    connection2.send(message.encode())

def main():
    print('Server is waiting for clients...')

    #box=tkinter.Tk()
    #box.mainloop()
    while True:
        #connect first client to server and send ACK back
        connection1,address1=serverSocket.accept()
        connection1.send(CONFIRM.encode())
        print(str(address1)+" has connected")
        print(connection1)

        #create new ClientPair object with first client
        clientPairN=ClientPair(address1,connection1)

        #connect second client to server and send ACK back
        connection2,address2=serverSocket.accept()
        connection2.send(CONFIRM.encode())
        print(str(address2)+" has connected")
        print(connection2)

        #add second client to ClientPair object
        clientPairN.addClient2(address2,connection2)

        #recieve usernames from both Clients
        username1=connection1.recv(1024).decode()
        username2=connection2.recv(1024).decode()
        clientPairN.addUsernames(username1,username2)

        #add ClientPair to list
        clientPairs.append(clientPairN)

        #start thread
        _thread.start_new(chatHandler,(clientPairN,))
        print(clientPairN.toString())

main()