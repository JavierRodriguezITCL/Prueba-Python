import socket 
import time

class Server:
     
    """
    Un servidor que recibe mensajes de texto.

    Attributes:
        HOST (string): la ip del servidor
        PORT (int): el puerto del servidor
        FORMATO(string): formato de codificación de los mensajes 
        HEADER(int): tamaño del header 
        ADRESS(tuple): Direción del servidor
    Methods:
        recibe(conn): Recibe los mensajes de la conexion y gestiona el tamaño del buffer dependiendo de la longitud del mensaje.
        main(): El servidor recibe los datos y los visualiza en el momento que le llegan con un timestamp.
        
    """
    HOST= '127.0.0.1'
    PORT = 12345
    FORMATO ='utf-8'
    HEADER = 64
    ADRESS=(HOST,PORT)


    def recibe (conn):
        """
        Recibe los mensajes de la conexion y gestiona el tamaño del buffer dependiendo de la longitud del mensaje.

        :param conn: la conexion.
        :type conn: conesxion de la libreria socket.
        :return: El mensaje recibido.
        :rtype: String con formato utf-8.

        """
        msg_length = conn.recv(Server.HEADER).decode('utf-8')
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(Server.FORMATO)
        return msg
            
        
    def main():
        """
        El servidor recibe los datos y los visualiza en el momento que le llegan con un timestamp.

        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sk:
            sk.bind(Server.ADRESS)
            sk.listen(1)
            cnn, addrs = sk.accept()

        while True:
            message=Server.recibe(cnn)
            if (message== "fin"):
                print(f"la communicacion con {addrs} termino")
                cnn.close()
                break  
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
            print(f'{timestamp}: Datos recibidos: {message}')
        sk.close()    

Server.main()