from socket import *

serverName = "130.136.5.36" #ip address
serverPort = 12001

clientSocket = socket(AF_INET, SOCK_DGRAM)
message = raw_input('Inserire frase in minuscolo: ')
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()
