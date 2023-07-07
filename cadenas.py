# # texto_variado=  "palabras 123 +- ##$%$"
# # print(type(texto_variado))

# #podemos utilizar comillas triples para que el texto se muestre como la cadena que hemos escrito
# print("""
# Funonamiento de programas: (opciones)
#     -1 Para acceder a opciones
#     -2 para salir
# """)

# #####################################################################################################
# #Subscripting e indexado

# texto= "Python"

# print(texto[0])
# print(texto[5])
# print(texto[-1])
# print(texto[-6])        #Se recorre hacia atras en la misma palabra pero no se puede rebasar los caracteres posicion no existe

# letra= texto[0] #Se guarda letra como P
# print(letra)

#     #texto[0]= "p" # Error! no podemos modificar una cadena

# letra= "p"
# print(letra)

# texto_compuesto= letra + texto[1]   #Concatenacion
# print(texto_compuesto)

# ######################################################################################################

# #Subcadenas Slicing o substringing
# texto= "Python"
# print(texto[0:3])
# print(texto[0:-3])
# print(texto[0:-2])
# print(texto[2:])    #se imprimen las palabras despues de la segunda letra de la palabra
# print(texto[:3])    #Se imprimen las palabras a la izquierda despues desde la 3 palabra

# print(texto[-3::-1])   #Cuenta menos 3 y va recorriendo una letra en una a la izquerda hasta terminar
# print(texto[::-1])      #Se escribe la palabra hacia atras de fianl a principio

# ##################################################################

# #Cadenas y formatos

# texto= "Hola mundo! Buenastardes"
# print(texto.lower())         #Se utilizan para hacer minusculas todas las letras del texto
# print(texto.upper())         #Todas las letras de texto pasan a ser MAYUSCULAS
# print(texto.capitalize())           #Solo la primera letra en mayuscula
# print(texto.title())            #Inicial de cada palabra se pone en mayuscula
# print(texto.swapcase())        #Intercambia las mayusculas por minusculas y viceversa
# texto= texto.upper()         #Cambia la variable texto a Mayusculas tener cuidado cuendo se cambien
# print(texto)

#Metodo format
print("{}+{}={}".format(2,3, 2+3))  #Sirve para meter valores
print("{}+{}={}".format("Hola", "mundo", "Hola mundo"))
print("{:.3f}+{:.4f}={}".format(2,3,2+3))                           # el numero .#f son los decimales con los que aparezca
print("{1}+{0}={2}".format(2,3,2+3))
print("{2}+{0}={1}".format("Hola","mundo","Hola mundo"))
print("{:d}={:b}={:o}={:x}".format(15,15,15,15))  #Decimal binario octal, exadecimal