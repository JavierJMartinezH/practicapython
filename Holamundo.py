while True:
        try:
            Salir = int(input(Fore.LIGHTBLUE_EX+"\nPara cerrar la calculadora escriba 1:  "))
    
        except ValueError:
            print(Fore.LIGHTRED_EX+"Debe escribir 1 para salir")
            continue
        if Salir<0:
            print(Fore.LIGHTRED_EX+"Debe escribir 1 para salir.")
            continue
        elif Salir>2:
            print(Fore.LIGHTRED_EX+"Debe escribir 1 para salir.")
            continue
        else:
            break