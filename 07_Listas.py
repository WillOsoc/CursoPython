lista01=[1,"dos",3,"cuatro",5]

lista01.append("seis")
lista01.insert(2,2.5)
lista01.extend([7,"ocho",9])
lista01.remove(2.5) 
lista01.pop()	#Elimina último elemento

lista02=["diez",11,"doce"]
lista03=lista01+lista02	#concatena las listas
lista04=lista03*2	# repite "n" veces la lista

print(lista01[2])
print(lista01[:]) #imprimir toda la lista
print(lista01[-2]) #imprime desde el final
print(lista01[0:3]) #imprimir desde:hasta --> incluye [0], excluye [3]
print(lista01[2:]) #imprimir desde [2] hasta el final
print(lista01.index("seis")) # en qué index está el elemento. Si hay varios, solo devuelve el primer index encontrado
print(9 in lista01) # si el elemento existe en la lista
print("diez" in lista01) # si el elemento existe en la lista

print(lista03[:])
print(lista04[:])