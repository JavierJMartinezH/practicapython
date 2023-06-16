nombre=input('¿Cómo te llamas?')
print('Hola '+ nombre)
apellido=input('¿Cual es tu apellido?')
print('Perfecto '+nombre,apellido)

edad=input('¿Cuantos años tienes?')
print(type(edad))
print(f"{nombre} {apellido} tiene {edad} años") # cadena de texto no se puede hacer operaciones

#programa que pide dos numeros al usuario
numero1=int(input('Introduce un número por favor:'))  #Si no se pone el int no los suma los concatena
numero2= int(input('introduce otro numero porfavor'))
numero3=numero1+numero2

print(f"El resultado de la suma es {numero3}")