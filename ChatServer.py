# This code was taken from TCPServer.py on the course canvas
from socket import *
import sys

args = sys.argv
if len(args) != 2:
    print ("Usage: python3 ChatServer.py port")
    exit()
port = int(args[1])

# Create welcoming socket using the given port
welcomeSocket = socket(AF_INET, SOCK_STREAM)
welcomeSocket.bind(('', port))
welcomeSocket.listen(1)

print ('Listening on port!', port, '...')

connectionSocket = None   # define it early so finally can access it

try:
    # While loop to handle arbitrary sequence of clients making requests
    while 1:
        # Waits for some client to connect and creates new socket for connection
        connectionSocket, addr = welcomeSocket.accept()
        print ('Client Made Connection')

        # Read input line from socket
        clientSentence = connectionSocket.recv(1024)
        clientSentence = clientSentence.decode()
        print ('FROM CLIENT:', clientSentence)

        # Capitalize the sentence
        serverSentence = clientSentence.upper()

        # Write output line to socket
        connectionSocket.send(serverSentence.encode())
        print ('TO CLIENT', serverSentence)

        # Close the connection socket
        connectionSocket.close()

except KeyboardInterrupt:
    print("\nShutting down server...")


finally:
    # Close the connection socket
    if(connectionSocket):
        connectionSocket.close()

    welcomeSocket.close()
    print("Server terminated.")