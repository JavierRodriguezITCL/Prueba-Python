from load import model, scaler_X, scaler_y
from run import InferenceEngine
import socket, time, glob, statistics
import pandas as pd


host = "127.0.0.1" # Tu ip como cliente BECKHOFF
server = "127.0.0.1" # La ip del servidor a donde te vas a conectar PC ITCL
port = 1234
counter = 0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server, port))

print("{}: Conectado al servidor".format(time.strftime('%x - %X')))


ie = InferenceEngine(model, scaler_X, scaler_y)



exec_time = [] #Lista de tiempos de ejecución 

while True:  
    try:
        
        data = str(s.recv(1024),"utf-8") # Bytes -> str

        if len(data) <= 0: #Si llega un envio vacio, corta el programa 
            break
        
        #print(counter)
        Lflo = [float(x) for x in data.replace('[','').replace(']','').split(',')] # Hay una manera mas elegante de convertir el str a float?

        print("{} Nuevo dato recibido: {}".format(time.strftime('%x - %X:'), Lflo))
        C1, C2, C3, C4, C5, C6 = Lflo[0], Lflo[1], Lflo[2], Lflo[3], Lflo[4], Lflo[5] # INPUTS FLOAT SEPARADOS PARA RED NEURONAL
        # LLAMADA A LA RED NEURONAL
        # Input format: F_PTO,      F_Mooring,  Vel_Cuerpo, Acc_Cuerpo, Pos_Cuerpo
        # Model format: Pos_Cuerpo, Vel_Cuerpo, Acc_Cuerpo, F_PTO,      F_Mooring
        start_time = time.time() #T ej start
        ie.predict([C6, C4, C5, C2, C3])
        PredH = ie.get_scaled_prediction()
        elapsed_time = time.time()-start_time #T ej stop
        #if elapsed_time != float(0):  #Los tiempos iniciales de la primera ventana van a ser 0 al recibirlos pero aun asi para el dataframe
        exec_time.append(elapsed_time)
        print(f"Tiempo de ejecución total: {elapsed_time} segundos")
        if PredH is not None:
            Predt = counter
            Pred = PredH, Predt # Los agrupo en un vector
            print("{} Prediccion calculada: {}. Enviado a control ...".format(time.strftime('%x - %X:'),Pred))
            Pred_raw = bytes(str(Pred),'utf-8') # Tuple -> Bytes. No hay otra manera de enviar por el socket que no sea en bytes, verdad?
            s.send(Pred_raw)
            print("{} Envio completado".format(time.strftime('%x - %X:')))
            
        counter = counter + 1
        
    
    except Exception as e:
        print("Fallo al recibir y procesar los datos...")
        print(e)
        time.sleep(2)
        break

#Prints para la documentacion-justificacion        
print()
print(f"La media de los tiempos de ejecución ha sido: {sum(exec_time)/len(exec_time)} segundos") 
print(f"La desviación estandar de los tiempos de comunicación ha sido: {statistics.pstdev(exec_time)} segundos") 
print()

#Construir el csv id | elapsed time
#df = {'Id':first_txt_column,'Inference_times':comm_time}
df = {'Inference_times':exec_time}
comm_df = pd.DataFrame(df)
comm_df.to_csv("Tiempos_inferencia.csv", encoding='utf-8', index=False)
print("Fichero csv generado con todos los tiempos de inferencia")
print()


#print(f"A la espera del siguiente fichero para procesar datos...")
time.sleep(1)
#break




s.close
print("{}: Desconectado del servidor".format(time.strftime('%x - %X:')))