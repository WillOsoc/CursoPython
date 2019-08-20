salario_presi=int(input("Introduce Salario de Presidente: "))
print("Salario Presidente: " + str(salario_presi))

salario_dire=int(input("Introduce Salario de Director: "))
print("Salario Director: " + str(salario_dire))

salario_jefe=int(input("Introduce Salario de Jefe: "))
print("Salario Jefe: " + str(salario_jefe))

salario_admin=int(input("Introduce Salario de Administrativo: "))
print("Salario Administrativo: " + str(salario_admin))

if salario_admin<salario_jefe<salario_dire<salario_presi:
	print("""******************
Todo está en orden
*******************""")
else:
	print("""******************
Algo no está bien
*******************""")