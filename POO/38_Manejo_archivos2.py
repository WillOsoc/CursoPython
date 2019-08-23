from io import open

text_file01=open("archivo.txt","r+") # "r+" para lectura y escritura

print(len(text_file01.read())) # Al leer completo, el cursor se queda al final del archivo

text_file01.seek(0)
print(text_file01.read(15)) # hasta el caracter 15

print(len(text_file01.read()))
text_file01.seek(len(text_file01.read())/2)
print(text_file01.read())

text_file01.seek(0)
print(len(text_file01.readlines()))  # len() con readlines, muestra cantidad de líneas

text_file01.seek(0)
text_file01.write("Inserto nuevo inicio\n")
print(text_file01.readlines())

text_file01.close()
del(text_file01)	# Liberar memoria, borrar fichero de la memoria

