import ScanUtility
import IpcClient
import BeaconProject
import sys

import bluetooth._bluetooth as bluez
import threading
from multiprocessing import Process, Pipe

dev_id = 0

def env_thread():
	print(sys._getframe().f_code.co_name," start")
    
    #Set bluetooth device. Default 0.
	try:
		sock = bluez.hci_open_dev(dev_id)
		#print ("\n *** Looking for BLE Beacons ***\n")
		#print ("\n *** CTRL-C to Cancel ***\n")
	except:
		print ("Error accessing bluetooth")

	ScanUtility.hci_enable_le_scan(sock)
	#Scans for iBeacons
	try:
		while True:
			returnedList = ScanUtility.parse_events(sock, 10)
			if(returnedList is not None):
				BeaconProject.stBeaconQue.put(returnedList)
				print(returnedList)
	except KeyboardInterrupt:
		pass

	return

print("start Thread")

threads = []

env_t = threading.Thread(target=env_thread)
threads.append(env_t)
env_t.start()

client_t = threading.Thread(target=IpcClient.ipcClient_thread)
threads.append(client_t)
client_t.start()



print("start Main")