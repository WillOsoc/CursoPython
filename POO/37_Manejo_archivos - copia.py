from io import open

frase="Primera frase\nhoy es martes"

# text_file01=open("archivo.txt","w")
# text_file01.write(frase)
# text_file01.close()

text_file02=open("archivo.txt","r")
texto=text_file02.read()
text_file02.close()
print(texto)

text_file03=open("archivo.txt","r")
text_lines=text_file03.readlines()
text_file03.close()
print(text_lines)

print("El arreglo tiene",len(text_lines),"items")

for i in text_lines:
	print(i)

text_file04=open("archivo.txt","a")
text_file04.write("\nagregamos otra línea\ny una más")
text_file04.close()