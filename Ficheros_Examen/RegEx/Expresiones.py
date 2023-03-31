import re

# Cargar el archivo de texto
with open('Ficheros_Examen/RegEx/auxi.txt', 'r', encoding="utf8") as f:
    text = f.read()
print(text)
# Contar cuantos "España.svg" hay en el texto
count_esp = len(re.findall(r'España\.svg', text))

# Sustituye todo lo que empiece por "Espa" y termine en ".svg" por "España.svg"
text = re.sub(r'Espa.*?\.svg', 'España.svg', text)

# Sustituye todo lo que empiece por mayúsculas y le sigan una o más minúsculas y termine en ".svg" por "España.svg"
text = re.sub(r'[A-Z][a-z]+\.svg', 'España.svg', text)

# Sustituye todo lo que termine en .svg por España.svg. 
#text = re.sub(r'.*?\.svg', 'España.svg', text)

# Sustituir todo lo que contenga cualquier cosa en el inicio, le siga números del 0 al 9 y continúe con ".svg" por "España.svg"
text = re.sub('^\d+\.svg', 'España.svg', text)

# Contar cuantos "España.svg" hay en el texto
count_esp_final = len(re.findall(r'España\.svg', text))

# Imprimir resultado
print (text)
print(f"Cantidad de 'España.svg' originalmente en el texto: {count_esp}")
print(f"Cantidad de 'España.svg' en el texto después de las sustituciones: {count_esp_final}")

# Comprobar resultado con un assert
assert count_esp_final == 8



