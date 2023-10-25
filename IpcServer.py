# Server code

import sys
import socket

UDP_IP = "127.0.0.1" # IP address of the server
UDP_PORT = 18001 # Port number of the server
def ipcServer_thread():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Create a UDP socket
    server_socket.bind((UDP_IP, UDP_PORT)) # Bind the socket with the IP address and port number

    while True:
        data, addr = server_socket.recvfrom(1024) # Receive data from the client
        print("Received message:", data.decode()) # Print the received message
        server_socket.sendto(b"Hello from server!", addr) # Send a response to the client

                