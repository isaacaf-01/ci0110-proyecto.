def CrearTableroVacio():
    tablero = [0,1,2,3,4,5,6,7]
    tablero[0] = ["~", "~", "~", "~", "~", "~", "~", "~"]
    tablero[1] = ["~", "~", "~", "~", "~", "~", "~", "~"]
    tablero[2] = ["~", "~", "~", "~", "~", "~", "~", "~"]
    tablero[3] = ["~", "~", "~", "~", "~", "~", "~", "~"]
    tablero[4] = ["~", "~", "~", "~", "~", "~", "~", "~"]
    tablero[5] = ["~", "~", "~", "~", "~", "~", "~", "~"]
    tablero[6] = ["~", "~", "~", "~", "~", "~", "~", "~"]
    tablero[7] = ["~", "~", "~", "~", "~", "~", "~", "~"]

    return tablero

def mostrar_tablero(matriz):
    print("")





    print ("holaaa")
    letras = "ABCDEFGH"
    print("    1   2   3   4   5   6   7   8") # Encabezado de números
    print("  +---+---+---+---+---+---+---+---+")
    
    for i in range(len(matriz)):              # este ciclo es para imprimir el tablero y sumarle el formato a la hora de mostrarlo en la terminal pero no van a ser parte de la matriz, solo es visual.
        fila = (letras[i] + " | ")
        for elemento in matriz[i]:
            fila += (elemento +  " | ")
        
        print(fila)
        print("  +---+---+---+---+---+---+---+---+")


def posicionar_barcos_Desctructor(matriz):
    while True:
        try:
    
            casilla = input("Indique la letra y luego el número donde desea colocar su barco\n(colocá un descructor / este barco ocupa dos casillas)\n").upper()
            orientacion_barco = input("Desea posicionarlo de manera vertical o horizontal?\n(Indique (v) si desea vertical o (h) si desea horizontal)\n")        
            letras = "ABCDEFGH"
        
            for i in range (0,8):
                if casilla[0] == letras[i]:
                    cordenada_x = i+1

            X = cordenada_x
            Y = int(casilla[1])
        
            if orientacion_barco == "v" or orientacion_barco == "V":
                if matriz[X-1][Y-1] == "~" and matriz[X][Y-1] == "~":
                    matriz[X-1][Y-1] = "B" 
                    matriz[X][Y-1] = "B"
                    break
                else:  
                    print("Ahí ya colocó un barco, Ingrese otra posición:")
           
                    mostrar_tablero(matriz)

            elif orientacion_barco == "h" or orientacion_barco ==  "H":

                if matriz[X-1][Y-1] == "~" and matriz[X-1][Y] == "~":     
                     
                    matriz[X-1][Y-1] = "B" 
                    matriz[X-1][Y] = "B"
                    break
                else:  
                    print("Ahí ya colocó un barco, Ingrese otra posición:")
           
                    mostrar_tablero(matriz)

            elif orientacion_barco != "h" or orientacion_barco != "H" or orientacion_barco != "V" or orientacion_barco != "v":
                print("Puede ingresar V o H solamente")
                  
        except ValueError:
            print("----------------------------------------------")
            print("Debe de ingresar una letra y luego un número")
            print("----------------------------------------------")
        except IndexError:
            print("------------------------------------------------------")
            print("El barco se sale del rango pruebe en otra posición")
            print("------------------------------------------------------")
        except Exception as e:
            print("----------------------------------")
            print("ocurrió un error inténtelo de nuevo")
            print("----------------------------------")
 

    mostrar_tablero(matriz)
        
        
    return matriz
    
    
def posicionar_barcos_acorazado(matriz):
    while True:
        try:
            casilla = input("Indique la letra y luego el número donde desea colocar su barco\n(colocá un acorazado / este barco ocupa cuatro casillas)\n" ).upper()
            orientacion_barco = input("Desea posicionarlo de manera vertical o horizontal?\n(Indique (v) si desea vertical o (h) si desea horizontal)\n")

            letras = "ABCDEFGH"
        
            for i in range (0,8):
                if casilla[0] == letras[i]:
                    cordenada_x = i+1

            X = cordenada_x
            Y = int(casilla[1])
        
            if orientacion_barco == "v" or orientacion_barco == "V":  
                if matriz[X-1][Y-1] == "~" and matriz[X][Y-1] == "~" and matriz[X+1][Y-1] == "~" and matriz[X+2][Y-1] == "~":
                    matriz[X-1][Y-1] = "B"
                    matriz[X][Y-1] = "B"
                    matriz[X+1][Y-1] = "B"
                    matriz[X+2][Y-1] = "B"
                    break
                else:
                    print("Ahí ya colocó un barco, Ingrese otra posición:")
           
                    mostrar_tablero(matriz)

                    

            elif orientacion_barco == "h" or orientacion_barco ==  "H":
                if matriz[X-1][Y-1] == "~" and  matriz[X-1][Y] == "~" and matriz[X-1][Y+1] == "~" and matriz[X-1][Y+2] == "~":
                    matriz[X-1][Y-1] = "B"
                    matriz[X-1][Y] = "B"
                    matriz[X-1][Y+1] = "B"
                    matriz[X-1][Y+2] = "B"
                    break
                else:
                    print("Ahí ya colocó un barco, Ingrese otra posición:")
           
                    mostrar_tablero(matriz)
            
            elif orientacion_barco != "h" or orientacion_barco != "H" or orientacion_barco != "V" or orientacion_barco != "v":
                print("Puede ingresar V o H solamente")
                    
            
        except ValueError:
            print("----------------------------------------------")
            print("Debe de ingresar una letra y luego un número")
            print("----------------------------------------------")
        except IndexError:
            print("------------------------------------------------------")
            print("El barco se sale del rango pruebe en otra posición")
            print("------------------------------------------------------")
        except Exception as e:
            print("----------------------------------")
            print("ocurrió un error inténtelo de nuevo")
            print("----------------------------------")
            
        
    mostrar_tablero(matriz)
    return matriz

def posicionar_barcos_submarinos(matriz):
    while True:       
        try:
            casilla = input("Indique la letra y luego el número donde desea colocar su barco\n(colocá un submarino / este barco ocupa tres casillas)\n" ).upper()
            orientacion_barco = input("Desea posicionarlo de manera vertical o horizontal?\n(Indique (v) si desea vertical o (h) si desea horizontal)\n")

            letras = "ABCDEFGH"
        
            for i in range (0,8):
                if casilla[0] == letras[i]:
                    cordenada_x = i+1

            X = cordenada_x
            Y = int(casilla[1])

            if orientacion_barco == "v" or orientacion_barco == "V":  
                if matriz[X-1][Y-1] == "~" and matriz[X][Y-1] == "~" and matriz[X+1][Y-1] == "~":
                
                    matriz[X-1][Y-1] = "B"
                    matriz[X][Y-1] = "B"
                    matriz[X+1][Y-1] = "B"
                    break
            
                else:
                    print("Ahí ya colocó un barco, Ingrese otra posición:")
           
                    mostrar_tablero(matriz)

        

            elif orientacion_barco == "h" or orientacion_barco ==  "H":
                if matriz[X-1][Y-1] == "~" and  matriz[X-1][Y] == "~" and matriz[X-1][Y+1] == "~":
               
                    matriz[X-1][Y-1] = "B"
                    matriz[X-1][Y] = "B"
                    matriz[X-1][Y+1] = "B"
                    break
                else:
                    print("Ahí ya colocó un barco, Ingrese otra posición:")
           
                    mostrar_tablero(matriz)

            elif orientacion_barco != "h" or orientacion_barco != "H" or orientacion_barco != "V" or orientacion_barco != "v":
                print("Puede ingresar V o H solamente")
        
        except ValueError:
            print("----------------------------------------------")
            print("Debe de ingresar una letra y luego un número")
            print("----------------------------------------------")
        except IndexError:
            print("------------------------------------------------------")
            print("El barco se sale del rango pruebe en otra posición")
            print("------------------------------------------------------")
        except Exception as e:
            print("----------------------------------")
            print("ocurrió un error inténtelo de nuevo")
            print("----------------------------------")

                
       
    mostrar_tablero(matriz)
    
    return matriz

def disparo_al_tablero (matriz_a,matriz_b): #hacer manejo excepciones 

    casilla = input("Indique la letra y luego el número donde desea disparar\n" ).upper()
    letras = "ABCDEFGH"
        
    for i in range (0,8):
        if casilla[0] == letras[i]:
                cordenada_x = i+1

    X = cordenada_x
    Y = int(casilla[1])

    if matriz_a[X-1][Y-1] == "B":

        matriz_b[X-1][Y-1] = "X"
        print("ha acertado a un barco")

    elif matriz_a[X-1][Y-1] == "~":

        matriz_b[X-1][Y-1] = "O"

        print("Ha disparado al gua ")

    mostrar_tablero(matriz_b)
    return matriz_b

def disparoTableroComputadora (matriz_a,matriz_b):
    import random
    X = random.randint(1,8)
    Y = random.randint(1,8)
    if matriz_a[X-1][Y-1] == "B":

        matriz_b[X-1][Y-1] = "X"
        print("la computadora ha acertado a un barco")

    elif matriz_a[X-1][Y-1] == "~":

        matriz_b[X-1][Y-1] = "O"

        print("La computadora ha disparado al gua ")

    return matriz_b

def posicionar_barcos_computadora(matriz):
    import random
    while True:
        X = random.randint(1, 8)
        Y = random.randint(1, 8)
        orientacion = random.randint(0, 1)
    
        if orientacion == 0: 
            if X <= 7: 
                if matriz[X-1][Y-1] == "~" and matriz[X][Y-1] == "~":
                    matriz[X-1][Y-1] = "B"
                    matriz[X][Y-1] = "B"
                    break 
    
        else:
            
            if Y <= 7:
                if matriz[X-1][Y-1] == "~" and matriz[X-1][Y] == "~":
                    matriz[X-1][Y-1] = "B"
                    matriz[X-1][Y] = "B"
                    break
        
    while True:
        
        X = random.randint(1, 8)
        Y = random.randint(1, 8)
        orientacion = random.randint(0, 1) 

        if orientacion == 0: 
            
            if X <= 5:
              
                if (matriz[X-1][Y-1] == "~" and matriz[X][Y-1] == "~" and matriz[X+1][Y-1] == "~" and matriz[X+2][Y-1] == "~"):
                    
                    matriz[X-1][Y-1] = "B"
                    matriz[X][Y-1] = "B"
                    matriz[X+1][Y-1] = "B"
                    matriz[X+2][Y-1] = "B"
                    break 

        else: 
            
            if Y <= 5:
                
                if (matriz[X-1][Y-1] == "~" and matriz[X-1][Y] == "~" and matriz[X-1][Y+1] == "~" and matriz[X-1][Y+2] == "~"):
                    
                    matriz[X-1][Y-1] = "B"
                    matriz[X-1][Y] = "B"
                    matriz[X-1][Y+1] = "B"
                    matriz[X-1][Y+2] = "B"
                    break 

    for submarinos in range(0,2):

        while True:
        
            X = random.randint(1, 8)
            Y = random.randint(1, 8)
            orientacion = random.randint(0, 1) 

            if orientacion == 0: 
            
                if X <= 6:
             
                    if (matriz[X-1][Y-1] == "~" and matriz[X][Y-1] == "~" and matriz[X+1][Y-1] == "~"):
                    
                        matriz[X-1][Y-1] = "B"
                        matriz[X][Y-1] = "B"
                        matriz[X+1][Y-1] = "B"
                        break 

            else:
           
                if Y <= 6:
                
                    if (matriz[X-1][Y-1] == "~" and matriz[X-1][Y] == "~" and matriz[X-1][Y+1] == "~"):
                    
                        matriz[X-1][Y-1] = "B"
                        matriz[X-1][Y] = "B"
                        matriz[X-1][Y+1] = "B"
                        break 

    
    return matriz                    

def partidaContraComputadora ():    

    print("Tablero jugador 1:")

    tablero_jugador1 = CrearTableroVacio()
    mostrar_tablero(tablero_jugador1)
    posicionar_barcos_Desctructor(tablero_jugador1)
    posicionar_barcos_acorazado(tablero_jugador1)
    for submarinos in range(0,2):
        posicionar_barcos_submarinos(tablero_jugador1)

    tablero_computadora = CrearTableroVacio()

    posicionar_barcos_computadora(tablero_computadora)

    print("---------------------------------")
    print("La computadora ya acomodó sus barcos")
    print("---------------------------------")

    tablero_disparos_jugador1 = CrearTableroVacio()
    tablero_disparos_jugador2 = CrearTableroVacio()
    tablero_disparos_computadora = CrearTableroVacio()
    contadorBarcosComputadora = 0
    contadorBarcosJugador1 = 0

    while True:
        disparo_al_tablero(tablero_computadora,tablero_disparos_jugador1)
        print("---------------------------------")
        disparoTableroComputadora(tablero_jugador1,tablero_disparos_computadora)    
        
    

if __name__== "__name__":  

    main() 

partidaContraComputadora()
       
#print("---------------------------------")
#print("Tablero jugador 2:")

#tablero_jugador2 = CrearTableroVacio()
#mostrar_tablero(tablero_jugador2)
#posicionar_barcos_acorazado(tablero_jugador2)
#posicionar_barcos_Desctructor(tablero_jugador2)
#for submarinos in range(0,2):
    #posicionar_barcos_submarinos(tablero_jugador2)


#print("los tablero quedaron así:\n")
#print("----------------------------------")
#print("jugador 1:")
#mostrar_tablero(tablero_jugador1)

#print("----------------------------------")
#print("jugador 2:")
#mostrar_tablero(tablero_jugador2)

#tablero_disparos_jugador1 = CrearTableroVacio()
#tablero_disparos_jugador2 = CrearTableroVacio()
#tablero_disparos_computadora = CrearTableroVacio()