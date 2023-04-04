import pickle as pk

try:
    with open("Ficheros_Examen/Pickle/model.pkl","rb") as fich:
        texto = fich.read()
except FileNotFoundError:
    print("Error: archivo no encontrado")
    texto = None

if texto:
    try:
        with open("Ficheros_Examen/Pickle/nuevo.pkl","wb") as nuevo:
            pk.dump(texto,nuevo)
    except:
        print("Error: fallo al escribir")
    else:
        try:
            with open("Ficheros_Examen/Pickle/nuevo.pkl","rb") as nuevo:
                lectura = pk.load(nuevo)
        except:
            print("Error: fallo al leer archivo")
        else:
            print(lectura)
else:
    print("Error: fallo al leer archivo")

""" No queda claro en el enunciado, si lo q se necesitaba era deserializar el archivo model.pkl o serializar este pese a ya estarlo.
En caso de haber sido la primera opción no se puede realizar debido a la incopatibilidad de versiones del sklearn. 
Yo no se que versión se utilizo para serializarlo, y esta claro que no fué la última"""