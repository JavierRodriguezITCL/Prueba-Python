import socket
import pandas as pd
import time

HOST= '127.0.0.1'
PORT = 12345

csk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


data = pd.read_csv('Test_numerico.txt', header=None,delim_whitespace=True)
csk.connect((HOST,PORT))
for i in range(1,2):
    for d in data[i]:
        csk.send(str(d).encode('utf-8'))
        time.sleep(10)
            
csk.send("fin".encode('utf-8'))
csk.close()
