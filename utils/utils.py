import numpy as np

import random

import time



def crear_tablero(casillas=10):
    """
    Crea un tablero de juego de tamaño 10 
    (salvo que se indique otra cosa) rellenado con "_".
    - casillas: longitud de la matriz cuadrada
    """
    return np.full((casillas, casillas), "_", dtype=str)


def ocultar_tablero(tablero):
    """
    Oculta los barcos no tocados ("O") en el tablero.
    Muestra solo los disparos acertados ("X") y los disparos al agua ('A').
    - Tablero: matriz en la que se juega
    """
    # Crear una copia del tablero para no modificar el original
    tablero_oculto = tablero.copy()
    
    # Recorre todas las posiciones del tablero
    for fila in range(tablero.shape[0]):
        for columna in range(tablero.shape[1]):
            if tablero[fila, columna] == 'O':  # Si hay un barco no tocado
                tablero_oculto[fila, columna] = '_'  # Se oculta con '_'
    
    return tablero_oculto


def crear_barco(eslora, tablero): 
    
    """ 
    Crea barcos de coordenadas aleatorias para un tablero por defecto de 10x10.
    - Eslora: será la longitud del barco
    - Tabblero: matriz en la que se juega
    """
    
    coordenadas = []      # lista vacia donde se almacenarán las coordenadas del barco
    orientacion = random.choice(["H","V"])  # Orientación que tendrá el barco en el tablero

    if orientacion == "H": 
        fila = random.randint(0, tablero - 1)       # genera un numero aleatorio para la fila
        columna = random.randint(0, tablero - eslora) # genera un numero aleatorio para la columna 
                                                        # teniendo en cuenta que no puede salirse del tablero
            
            # Recorre el rango de la eslora indicada
        for i in range(eslora):     
            coordenadas.append((fila, columna + i))  # Añade a la lista vacia de coordenadas la fila generada y la columna + i
    
    if orientacion == "V":
        fila = random.randint(0, tablero - eslora)       # genera un numero aleatorio para la fila
        columna = random.randint(0, tablero - 1) # genera un numero aleatorio para la columna 
                                                        # teniendo en cuenta que no puede salirse del tablero
            
            # Recorre el rango de la eslora indicada
        for i in range(eslora):     
            coordenadas.append((fila + i, columna)) 
    
    return coordenadas   


def colocar_barco(barco, tablero):
    """
    Coloca un barco en el tablero.
    - barco: coordenadas (tuplas) donde se colocará el barco.
    - tablero: Tablero donde se colocará el barco.
    """
    # Recorre la lista de tuplas (coordenadas del barco)
    for fila, columna in barco:
        if tablero[fila, columna] != "_":   # Comprueba que en esa coordenada no hay un "_" 
                                            # y devuelve el error con la información
            raise ValueError(f"Ya hay un barco en la posición ({fila}, {columna})")
        tablero[fila, columna] = "O"  # Si no hay barco coloca una "O" en esa posición
    return tablero


def verificar_hundido(casilla, tablero, barcos):
    """
    Comprueba si el disparo actual ha hundido un barco.
    - tablero: Tablero del jugador o del oponente.
    - barcos: Lista de las posiciones de los barcos.
    - casilla: Coordenadas del disparo.
    """
    for barco in barcos:
        if casilla in barco:  # Si el disparo pertenece a este barco
            hundido = True  # Empezamos dando por hecho el barco está hundido como hundido
            for fila, columna in barco:  # Recorremos todas las posiciones del barco
                if tablero[fila, columna] != 'X':  # Si alguna no está marcada como 'X'
                    hundido = False  # Cambiamos hundido a False
                    break  # Y terminamos el  bucle
            
            if hundido:  # Si hundido lo hemos mantenido en True:
                print("Tocado y hundido!")
            else:
                print("¡Tocado!")


def disparar(casilla, tablero, barcos):
    """
    Realiza un disparo en la casilla especificada.
    - casilla: Tupla (fila, columna) donde se dispara.
    - tablero: Tablero donde se evalúa el disparo.
    """

    fila, columna = casilla
    if tablero[fila, columna] == "O": # Si en esa posicion hay una "O" lo marca con "X" e indica tocado
        tablero[fila, columna] = "X"
        verificar_hundido(casilla, tablero, barcos)
        resultado = "Tocado"     
    elif tablero[fila, columna] == "_":  # Si en esa posicion hay un "_" la marca con "A" e indica agua
        tablero[fila, columna] = "A" 
        resultado = "Agua"
        print(f"Agua!")
    
    else:
        print(f"Ya has disparado a {casilla}, más atento la proxima vez") # Si se encuentra otra cosa que no sea "O" o "_" 
        resultado = "Repetido"                                                                  # indica que esa coordenada ya ha sido disparada
    
    return resultado                          




def colocar_barcos(tablero):
    """
    Coloca 6 barcos en el tablero.     
    Si ocurre un ValueError por superposición, resetea el tablero y vuelve a generar y colocar los barcos.
    - tablero: matriz donde se colocan los barcos

    """
    barcos = []

    while True:
        try:
                
            # Generar los barcos
            barco1 = crear_barco(2, tablero.shape[0])
            barco2 = crear_barco(2, tablero.shape[0])
            barco3 = crear_barco(2, tablero.shape[0])
            barco4 = crear_barco(3, tablero.shape[0])
            barco5 = crear_barco(3, tablero.shape[0])
            barco6 = crear_barco(4, tablero.shape[0])

            
            # Intentar colocarlos en el tablero
            colocar_barco(barco1, tablero)
            colocar_barco(barco2, tablero)
            colocar_barco(barco3, tablero)
            colocar_barco(barco4, tablero)
            colocar_barco(barco5, tablero)
            colocar_barco(barco6, tablero)

            barcos.extend([barco1, barco2, barco3, barco4, barco5, barco6])

            return tablero, barcos
        
        # Si se encuentra con ValueError (ya hay un barco en esa posición)  resetea el 
        # tablero y vuelve a intentar generar y colocar los barcos
        except ValueError:
            tablero[:] = '_' 



def turno_ordenador(tablero_jugador):
    """
    Genera unas coordenadas aleatorias del ordenador para disparar al tablero del jugador.
    - Tablero_jugador: matriz de juego donde están colocados los barcos del jugador
    """

    longitud = tablero_jugador.shape[0]   # La longitud es igual al numero de columnas del tablero

    # Bucle "infinito" para que genere una coordednadaa valida
    while True: 
        fila = random.randint(0, longitud - 1)  # Numero aleatorio de fila
        columna = random.randint(0, longitud - 1)  # Numero aleatorio de columna
        if tablero_jugador[fila, columna] not in ('X', 'A'):  # Si en coordenadas no hay X ni A continua
            return (fila, columna)
        


def tablero_legible(tablero):
    """
    Muestra el tablero sin corchetes para que sea más visual.
    - tablero: matriz donde están colocados barcos del jugador o del oponente

    """
    
    resultado = ""
    for fila in tablero:
        resultado += " ".join(fila) + "\n"

    return resultado


def chuleta():
    """
    Genera una plantilla del tablero donde se indica el indice de cada fila y columna.
    """

    tablero_jugador = [["0 ", "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_"],
            ["1 ", "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_"],
            ["2 ", "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_"],
            ["3 ", "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_"],
            ["4 ", "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_"],
            ["5 ", "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_"],
            ["6 ", "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_"],
            ["7 ", "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_"],
            ["8 ", "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_"],
            ["9 ", "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_" , "_"]]
    filas_jugador = ["", "0","1","2", "3", "4", "5", "6", "7", "8", "9"]

    print("\n ", *filas_jugador) 
    for fila in tablero_jugador:
        print(*fila)

