from load import model, scaler_X, scaler_y
from run import InferenceEngine
import socket, time, glob, statistics
import pandas as pd


host = "127.0.0.1"
server = "127.0.0.1" 
port = 1234
counter = 0
#Cree la estructura de conexion al socket

print("{}: Conectado al servidor".format(time.strftime('%x - %X')))



exec_time = [] #Lista de tiempos de ejecución 

while True:  
    # xx a completar
    #
      
print()
print(f"La media de los tiempos de ejecución ha sido: {sum(exec_time)/len(exec_time)} segundos") 
print(f"La desviación estandar de los tiempos de comunicación ha sido: {statistics.pstdev(exec_time)} segundos") 
print()


df = {'times':exec_time}
comm_df = pd.DataFrame(df)
comm_df.to_csv("Tiempos.csv", encoding='utf-8', index=False)

time.sleep(1)
