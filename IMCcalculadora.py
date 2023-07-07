from colorama import init, Fore, Back, Style
init()
        #Calculadora de Indice de Masa Corporal(IMC) realizada por "Javier José Martínez Hernández"

#Realizamos en esta parte una pequeña presentacion de nuestro programa
print(Fore.LIGHTMAGENTA_EX+"\n\tEstas usando la Calculadora de Índice de Masa Corporal (IMC) ")
print(Fore.BLUE+"\n\tRealizado por:\n\t\tJavier José Martínez Hernández")

#Empezamos nuestra calculadora de IMC pidiendo la cantidad de personas que por medio del while hacemos que nuestras condiciones se
#cumplan y no podamos ingresar datos erroneos a nuestro programa, en esta ocasion se limito a 6 personas aunque puede configurarse
#para ingresar mas personas.
while True:
        try:
            personas = int(input(Fore.GREEN+"\n¿A cuantas personas quiere calcular su IMC?   "))
    
        except ValueError:
            print(Fore.LIGHTRED_EX+"Debe escribir un número.")
            continue
        if personas<0:
            print(Fore.LIGHTRED_EX+"Debe escribir un número positivo,")
            continue
        elif personas>6:
            print(Fore.LIGHTRED_EX+"Limitado a 6 personas por el Operador Javier")
            continue
        else:
            break
#-----------------------------------------------------------------------------------------------------

#Por medio de este while realizamos el ciclo de las personas ingresadas permitiéndonos aplicar las 
    #condiciones que nos permiten no rebasar el número de personas ingresadas
while personas > 0:
    #-------------------------------------------------------------------------------------------------
    #Se realiza la validación del nombre introducido de la persona 
        #con lo que solo nos deja introducir texto y nos manda un mensaje si se introduce otro formato
    while True:
        nombre = input(Fore.LIGHTBLUE_EX+"Ingrese su nombre: ") 
        lista_nombre = []
        nombre_separado = nombre.split(" ")
        for i in range(0, len(nombre_separado)):
            if nombre_separado[i].isalpha() == True:
                lista_nombre.append(nombre_separado[i])
        s = "".join(nombre_separado)
        if s.isalpha() == False:
            print(Fore.LIGHTRED_EX+"El nombre no es válido, digite su nombre real")
        if s.isalpha() == True:
            nombre = nombre.title()
            break
    #-------------------------------------------------------------------------------------------------    
        #Se realiza la validación del apellido paterno introducido de la persona 
            #con lo que solo nos deja introducir texto y nos manda un mensaje 
            #si se introduce otro formato
    while True:
        ap = input(Fore.LIGHTBLUE_EX+"Ingrese su apellido paterno: ")
        lista_ap = []
        ap_separado = ap.split(" ")
        for i in range(0, len(ap_separado)):
            if ap_separado[i].isalpha() == True:
                lista_ap.append(ap_separado[i])
        s = "".join(ap_separado)
        if s.isalpha() == False:
            print(Fore.LIGHTRED_EX+"El apellido paterno no es válido, digite su apellido real")        
        if s.isalpha() == True:
            ap = ap.title()
            break
    #-------------------------------------------------------------------------------------------------
    #Se realiza la validación del apellido materno introducido de la persona 
        #con lo que solo nos deja introducir texto y nos manda un mensaje 
        #si se introduce otro formato            
    while True:
        am = input(Fore.LIGHTBLUE_EX+"Ingrese su apellido materno: ")
        lista_am = []
        am_separado = am.split(" ")
        for i in range(0, len(am_separado)):
            if am_separado[i].isalpha() == True:
                lista_am.append(am_separado[i])
        s = "".join(am_separado)
        if s.isalpha() == False:
            print(Fore.LIGHTRED_EX+"El apellido materno no es válido, digite su apellido real")
        if s.isalpha() == True:
            am = am.title()
            break
    #-------------------------------------------------------------------------------------------------
    #Se pide la edad en numero entero (int) por lo que no permitirá ingresar letras 
        #y se limito a la edad de 122 ya que es el registro de la persona más longeva 
        #en la historia.
    while True:
        try:
            edad = int(input(Fore.LIGHTBLUE_EX+"Ingrese su edad en años: "))
    
        except ValueError:
            print(Fore.LIGHTRED_EX+"Debe escribir su edad en número.")
            continue
        if edad<=0:
            print(Fore.LIGHTRED_EX+"Debe escribir un numero positivo o mayor a 0.")
            continue
        elif edad>122:
            print(Fore.LIGHTRED_EX+"Debe escribir su verdadera edad.")
            continue
        else:
            break
    #-------------------------------------------------------------------------------------------------
    #Nuestra variable de altura esta en forma de metros por lo que se puso el formato de float 
        #para poder ingresar decimales y se limito a una altura máxima de 2.72 ya que es el registro 
        #mas alto en la historia.
    while True:
        try:
            altura = float(input (Fore.LIGHTBLUE_EX+"Ingrese su altura en metros: "))
        except ValueError:
            print(Fore.LIGHTRED_EX+"Debe escribir la altura correcta.")
            continue
        if  altura<=0:
            print(Fore.LIGHTRED_EX+"Debe escribir un número positivo o mayor a cero.")
            continue
        elif altura>2.72:
            print(Fore.LIGHTRED_EX+"Debe escribir un número menor a 2.72.")
        else:
            break
    #-------------------------------------------------------------------------------------------------
    #El peso está en kilogramos por lo que se puso el formato de float para poder 
        #ingresar decimales y se limitó a un peso máxima de 594.8 ya que es el registro más alto en la historia.
    while True:
        try:
            peso = float(input(Fore.LIGHTBLUE_EX+"Ingrese su peso en kilogramos:"))
        except ValueError:
            print(Fore.LIGHTRED_EX+"Debe escribir el peso en kilogramos.")
            continue
        if  peso<=0:
            print(Fore.LIGHTRED_EX+"Debe escribir un número positivo o mayor a cero.")
            continue
        elif peso>594.8:
            print(Fore.LIGHTRED_EX+"Debe escribir un número menor.")
        else:
            break
    #-------------------------------------------------------------------------------------------------
    #Con esta formula realizamos el calculo del IMC, masa=(Peso en kilogramos) entre 
        #la estatura (altura en metros) elevada al cuadrado
    IMC = peso / altura**2
    #-------------------------------------------------------------------------------------------------
    #Imprimimos los valores ingresados de la persona y su resultado de su calculo de IMC peromitiendole 
        #saber en que estado se encuentra esta parte se muestra de diferente color simulando los colores 
        #de un semaforo dependiendo el resultado

    print(Fore.LIGHTMAGENTA_EX+"\nSu nombre completo es: "+ Fore.LIGHTGREEN_EX+str(nombre+" "+ap+ " "+am))
    print(Fore.LIGHTMAGENTA_EX+"Su edad: "+ Fore.LIGHTGREEN_EX+str(edad)+" años")
    print(Fore.LIGHTMAGENTA_EX+"Su altura es: "+ Fore.LIGHTGREEN_EX+str(altura)+" m")
    print(Fore.LIGHTMAGENTA_EX+"Su peso es: "+ Fore.LIGHTGREEN_EX+str(peso)+" kg")
    print(Fore.YELLOW+"IMC: " + str(IMC) )

    #-------------------------------------------------------------------------------------------------
    #Estas son las validaciones que se realiza en el resultado para saber su condición.
    if IMC >= 0 and IMC <= 15.99 :
        print (Fore.LIGHTRED_EX+"Delgadez severa")
    elif IMC >= 16.00 and IMC <= 16.99 :
        print (Fore.RED+"Delgadez moderada")
    elif IMC >= 17.00 and IMC <= 18.49:
        print (Fore.LIGHTYELLOW_EX+"Delgadez leve")
    elif IMC >= 18.50 and IMC <= 24.99 :
        print (Fore.LIGHTGREEN_EX+"Normal")
    elif IMC >= 25.00 and IMC <= 29.99:
        print (Fore.LIGHTYELLOW_EX+"Sobrepeso")
    elif IMC >= 30.00 and IMC <= 34.99:
        print (Fore.RED+"Obesidad leve")
    elif IMC >= 35.00 and IMC <= 39.00:
        print (Fore.RED+"Obesidad media")
    elif IMC >= 40.00:
        print (Fore.LIGHTRED_EX+"Obesidad morbida")
    
    #Se expresa esta formula para asi poder hacer que la condicion de nuestro while de personas ingresadas 
        #sean las que realmente queremos ingresar ya que si no se realiza se vuelve un ciclo infinito
    personas = personas - 1
#---------------------------------------------------------------------------------------------------------
#Esta sección es para que el programa no se cierre al instante de mostrar la pantalla de los valores ingresados
print(Fore.LIGHTGREEN_EX+"\n\t\tMuchas gracias por usar la calculadora de IMC")

while True:
        try:
            Salir = int(input(Fore.LIGHTBLUE_EX+"\nPara cerrar la calculadora escriba 1:  "))
    
        except ValueError:
            print(Fore.LIGHTRED_EX+"Debe escribir 1 para salir")
            continue
        if Salir<1:
            print(Fore.LIGHTRED_EX+"Debe escribir 1 para salir.")
            continue
        elif Salir>1:
            print(Fore.LIGHTRED_EX+"Debe escribir 1 para salir.")
            continue
        else:
            break
#Reflexión:
#       En esta fase del bootcamp pude aprender de forma eficiente los pasos para poder realizar el proyecto
#       correspondiente por lo que me siento contento de lo logrado en la realización del mismo, la practica
#       me permitió llegar a la meta de la realizacion de mi Calculadora de IMC y comprender la estructura
#       con la que se compone.