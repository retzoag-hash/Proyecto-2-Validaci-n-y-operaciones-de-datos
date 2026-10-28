####################### 1. Longitud de una frase ############


cantidad = 0 #definimos la variable
while cantidad <20: # while = mientras la cantida se menor que 20
    palabra = input('ingresa la palabra que tenga entre 4 a 8 letras: ') # definimos la variable palabra con la input=entrada del texto 
    cantidad = len(palabra) #contamos la longitud=len de la variable palabra 
    if cantidad > 8: #if = si cantidad es mayor que 8 
     print('Sobran letras. ''Tiene', len(palabra) ,'letras') # imprimimos  
    elif cantidad < 4: # elif = si no si cabtida es mayor que 4 
      print('Hace falta letras. ''Solo tiene', len(palabra),'letras') # imprimimos
      continue # continue evita lo de abajo e inicia el ciclo
    elif cantidad >= 4: # si no si cantidad es mayor o igual que cuatro
        print('Palabra correcta')# imprimimos
        break # break = salir del ciclo 
    else:  # else = si no se cumplen ninguna condicion 
        print('siga las istrucciobes de favor') # imprimimos
print('La palabra es:' ,palabra ,'contiene:', len(palabra),'letras' )



##################### 2. Encuentra el cuadrante ##############################


Cuadrante = ['I','II','III','IV'] # definimos un lista con los nombres de los valores

co_X = int(input('Ingrese X : ')) #  definimos los valores x
co_Y = int(input('Ingrese Y : ')) #  definimos los valores y

if co_X > 0 and co_Y >0:   #  si con_x es mayor que cero y co_y es mayor que cero
    print('El punto se encuentra en el cuadrante',(Cuadrante[0])) # imprimir cuadrante  que se encutra en la lista en la posicion 0
elif co_X < 0 and  co_Y <0:  #  si no si con_x es menor que cero y co_y es menor que cero
    print('El punto se encuentra en el cuadrante',(Cuadrante[2])) # imprimir cuadrante  que se encutra en la lista en la posicion 2
elif co_X > 0 and co_Y <0:   #  si no si con_x es mayor  que cero y co_y es menor que cero
    print('El punto se encuentra en el cuadrante',(Cuadrante[3])) # imprimir cuadrante  que se encutra en la lista en la posicion 0
elif co_X < 0 and co_Y >0:  #  si no si con_x es menor que cero y co_y es mayor que cero
    print('El punto se encuentra en el cuadrante',(Cuadrante[1])) # imprimir cuadrante  que se encutra en la lista en la posicion 0
else: # si no ocurre nada de lo aterior
    print('No esta dentro de los parmetros establecidos') # imprimi esto
    