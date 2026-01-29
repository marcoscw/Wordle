#Creo la funcion para solicitar y validar la palabra de intento
def solicitar_palabra():
    while True:
        word = input("Introduzca una palabra de 5 letras")
        if(len(word) != 5):
            print("La palabra tiene que ser de 5 letras")
        else:
            return word.upper() #Dejar la palabra en mayuscula por default
            

#DEFINICION DEL CODIGO DEL JUEGO
def wordle():
    palabra_del_dia = 'CARPA'
    dict_palabra = {}
    #hacer un recuento de la cantidad de letras especificas en la palabra del dia y las guarda en un dicc
    for letra in palabra_del_dia:
        if letra in dict_palabra:
            dict_palabra[letra] = dict_palabra.get(letra) + 1 #si ya existe se le suma 1 valor
        else:
            dict_palabra[letra] = 1 #si no existe aun la letra en el diccionario se le asigna el valor de 1
    
    #Empiezan los 5 intentos posibles
    for intento in range(5) : #5 intentos
        #reseteo el diccionario de la palabra secreta por cada intento
        dict_palabra_temp = dict_palabra.copy()   
        
        #Llamo a la funcion para solicitar y verificar la palabra
        word = solicitar_palabra()
        #Logica General del Juego
        '''En caso de que la letra este en la posicion correcta se pondra en verde, en caso 
        de que la letra se encuentre en la palabra se pondra en naranja, sino, la letra quedara igual'''
        #"\033[<style>;<fg>;<bg>mTu texto\033[0m"
        #Primero se controla que la palabra sea la correcta directamente;
        if(word == palabra_del_dia):
            for letter in word:
                print(f"\033[0;32;40m\033[m",end = ' ')
            print("Tu palabra es correcta!!")
            return
        else:
            #La primera vez recorre y resta de mi diccionario la cantidad de la letra "letter" si es que coincide su posicion
            for index,letter in enumerate(word):
                if(letter == palabra_del_dia[index]):
                    dict_palabra_temp[letter] = dict_palabra_temp[letter] - 1

            #la segunda vez recorre y va imprimiendo en verde las letras coincidentes sin restar, 
            #se imprimen en naranja si las letras existen en la palabra y se resta 1
            #si no existen en la palabra no cambia de color
            for index,letter in enumerate(word_as_list):
                if(letter == palabra_del_dia[index]):
                    #IMPRIME EN COLOR VERDE LA LETRA COINCIDENTE CON LA POSICION
                    print(f"\033[0;32;40m{letter}\033[0m", end=" ")
                elif letter in dict_palabra_temp and dict_palabra_temp[letter] != 0:
                    #IMPRIME EN COLOR NARANJA LA LETRA EXISTENTE PERO FUERA DE POSICION
                    dict_palabra_temp[letter] = dict_palabra_temp[letter] - 1
                    print(f"\033[0;33;40m{letter}\033[0m", end=" ")        
                else:
                    print(letter,end=" ")
            print()
    
    #Si terminan los 5 intentos se imprime el final del juego
    print("Se acabaron tus intentos")


#EJECUCION DE LA FUNCION WORDLE
wordle()
