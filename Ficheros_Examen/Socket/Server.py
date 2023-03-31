import socket 
import time
import pandas as pd
HOST= '127.0.0.1'
PORT = 12345
host_addr=(HOST,PORT)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sk:
    sk.bind(host_addr)
    sk.listen(10)
    cnn, addrs = sk.accept()

    while True:
        message=cnn.recv(1024).decode('utf-8')
        if (message== "fin"):
            print(f"communication with {addrs} ended")
            cnn.close()
            break  
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        print(f'{timestamp}: Datos recibidos: {message}')
    sk.close()    


