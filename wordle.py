#Creo la funcion para solicitar y validar la palabra de intento
def solicitar_palabra():
    while True:
        word = input("Introduzca una palabra de 5 letras")
        if(len(word) != 5):
            print("La palabra tiene que ser de 5 letras")
        else:
            return word.upper() #Dejar la palabra en mayuscula por default
            
