# Client code
import sys
import BeaconProject
import socket
import json
from time import sleep

UDP_IP = "127.0.0.1" # IP address of the server
UDP_PORT = 18001 # Port number of the server

def ipcClient_thread():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Create a UDP socket
    while(1):
        if(BeaconProject.stBeaconQue.empty() == False):
            for element in BeaconProject.stBeaconQue.get():
                sBeacon = ""
                for key, val in element.items():
                    temp = "{key}: {value},".format(key=key,value=val)
                    #print("{key}: {value}".format(key=key,value=val))
                    if(key == 'uuid' or key == 'major' or key == 'minor' or key == 'macAddress'):
                        sBeacon += temp;
                #print(sBeacon)    
                sbuff = sBeacon.encode('utf-8')
                #print(type(sbuff))
                #print(sbuff)
            client_socket.sendto(sbuff, (UDP_IP, UDP_PORT)) # Send a message to the server
        sleep(0.1)
        

