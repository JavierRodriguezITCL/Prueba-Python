import pickle as pk

fich = open("Ficheros_Examen/Pickle/model.pkl","rb")
texto= fich.read()

nuevo = open("Ficheros_Examen/Pickle/nuevo.pkl","wb")
pk.dump(texto,nuevo)
nuevo.close()

nuevo = open("Ficheros_Examen/Pickle/nuevo.pkl","rb")
lectura = pk.load(nuevo)
print(lectura)
nuevo.close()
fich.close()

""" No queda claro en el enunciado, si lo q se necesitaba era deserializar el archivo model.pkl o serializar este pese a ya estarlo.
En caso de haber sido la primera opción no se puede realizar debido a la incopatibilidad de versiones del sklearn. 
Yo no se que versión se utilizo para serializarlo, y esta claro que no fué la última"""