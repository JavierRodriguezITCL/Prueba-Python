import socket
import pandas as pd
import time
class Client:
    """
    Unc cliente que envía mensajes a un servidor leidos de un archivo de texto.

    Attributes:
        HOST (string): la ip del servidor
        PORT (int): el puerto del servidor
        FORMATO(string): formato de codificación de los mensajes 
        HEADER(int): tamaño del header 
        ADRESS(tuple): Direción del servidor
        csk (socket.socket): Socket para la conexión
    Methods:
        envia(msg): Envia un mensaje al servidor, enviando primero un mensaje indicando la longitud del mensaje.
        termina(): Envia un mensaje que informa de la terminación del envio de datos y cierra la conexión.
        main(): Envia un dato leido del fichero al servidor cada 10 segundos.
    """
    HOST= '127.0.0.1'
    PORT = 12345
    FORMATO ='utf-8'
    HEADER = 64
    ADRESS = (HOST,PORT)
    csk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    @staticmethod
    def envia(msg):
        """
        Envia un mensaje al servidor, enviando primero un mensaje indicando la longitud del mensaje.

        :param msg: El mensaje a enviar.
        :type msg: variable.
        """
        message = str(msg).encode(Client.FORMATO)
        msg_length = len(message)
        send_length = str(msg_length).encode(Client.FORMATO)
        send_length += b' ' * (Client.HEADER - len(send_length))
        Client.csk.send(send_length)
        Client.csk.send(message)

    @staticmethod
    def termina():
        """
        Envia un mensaje que informa de la terminación del envio de datos y cierra la conexión.

        """
        Client.csk.send(str(3).encode('utf-8'))
        Client.csk.send("fin".encode('utf-8'))
        Client.csk.close()

    @staticmethod
    def main():
        """
        Envia un dato leido del fichero al servidor cada 10 segundos.

        """
        data = pd.read_csv('Test_numerico.txt', header=None,delim_whitespace=True)
        Client.csk.connect(Client.ADRESS)
        for i in range(1,6):
            for d in data[i]:
                Client.envia(d)
                time.sleep(0.5)
        Client.termina()    

Client.main()        