from colorama import init, Fore, Back, Style
init()

def obtenerDatos ():

    while True:
        nombre = input("Digite su nombre: ")
          
        lista_nombre = []

        nombre_separado = nombre.split(" ")

        for i in range(0, len(nombre_separado)):
            if nombre_separado[i].isalpha() == True:
                lista_nombre.append(nombre_separado[i])
        
        s = "".join(nombre_separado)
        
        if s.isalpha() == False:
            print("El nombre no es válido, digite su nombre real")
            print()
        
        if s.isalpha() == True:
            print()
            nombre = nombre.title()
            nombre = (f"Su nombre es: {nombre}")
            print(nombre)
            break
obtenerDatos()

