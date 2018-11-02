import socket
import _thread
serverPort = 9999

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientPairs = []

serverSocket.bind(('', serverPort))


# def findPartner(address):
#     count = 0
#     clients = len(clientPairs)
#     for item in clientPairs:
#         if address != item:
#             count += 1
#     if count == clients:
#         clientPairs.append(address)

class ClientPair:
    def __init__(self,client1Address, client1Name):
        self.client1Add=client1Address
        self.client1Name=client1Name
        self.client2Add=0
        self.client2Name=''

    def addClient2(self,client2Address,client2Name):
        self.client2Add=client2Address
        self.client2Name=client2Name



def clientHandler(address,name):
    confirmation='Client Connected to Server'
    serverSocket.sendto(confirmation.encode(),address)

    if len(clientPairs)==0:
        clientPair=ClientPair(address,name)
        clientPairs.append(clientPair)
    else:
        clientPairs[0].addClient2(address)
        message='You are connected with '+ clientPairs[0].client1Name
        serverSocket.sendto(message.encode(),address)

    # while True:





def main():
    print('Server is waiting for clients...')

    while True:

        message, address = serverSocket.recvfrom(1024)



