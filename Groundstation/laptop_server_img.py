import socket
import sys
import cv2
import pickle
import numpy as np
import struct ## new
import time

# Change the host ip address and port number 
HOST='192.168.66.117'
PORT=8089

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created')

s.bind((HOST,PORT))
print('Socket bind complete')
s.listen(10)
print('Socket now listening')

conn,addr=s.accept()

### new
data = bytearray()
payload_size = struct.calcsize("L") 
while True:
    while len(data) < payload_size:
        data += conn.recv(4096)
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("L", packed_msg_size)[0]
    while len(data) < msg_size:
        data += conn.recv(4096)
    frame_data = data[:msg_size]
    data = data[msg_size:]
    ###
    frame=pickle.loads(frame_data)
    if(frame.any() != None ):
        cv2.imshow('frame',frame)
        cv2.waitKey(1)
    
    #print(frame)
    #time.sleep(0.3)
    

