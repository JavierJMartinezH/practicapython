#Ejemplos de la función print()

print("Hola mundo")
print('Hola mundo','otra vez')
print('Son las',9,'de la mañana')
print('El resultado de 3*4 es:',3*4)

#Ejemplo de cadenas formateadas
print('El número 15 en sistema decimal es %d, en sistema octal es %o, en el sistema hexadecimal es %x' %(15,15,15))

pi=3.141592
r=5
print(f'El radio de un circulo es {r} y el área de ése circulo es {pi*r**2:.2f}')   #f para cadena formateada

#Impresion de caracteres especiales
print('La letra beta es: \n\t \u03B2') #Salto de linea \n y tabulación es \t    \u03B2 codigo askii de Beta

#caracteres de escape
print('Hola mundo', end='')
print('otra vez', end = '\t')
print('y otra vez')