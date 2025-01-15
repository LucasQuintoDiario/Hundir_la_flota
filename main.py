from utils import *

# Se crean los dos tableros de juego y listas necesarias para jugar

tablero_jugador = crear_tablero()
tablero_oponente = crear_tablero()
tablero_conbarcos_oponente = colocar_barcos(tablero_oponente)
barcos_oponente = tablero_conbarcos_oponente[1]

print("""HUNDIR LA FLOTA
Antes de comenzar a jugar veamos unas cuestiones basica sobre el funcionamiento.      
Este es tu tablero de juego:
    """)

time.sleep(1)


# Se imprime el tablero del jugador
print(tablero_legible(tablero_jugador))

# Se colocan los barcos en el tablero y se crea la lista de coordenadas de todos los barcos
tablero_conbarcos_jugador = colocar_barcos(tablero_jugador)
barcos_jugador = tablero_conbarcos_jugador[1]

time.sleep(2)

print("""\nLo primero que vamos a hacer es colocar tus barcos en él.
En esta versión jugaremos con 6 barcos que estarán representados con 
una 'O' en el tablero:
    
- 3 de eslora 2
- 2 de eslora 3
- 1 de eslora 4
    """)

time.sleep(2)

#Se colocan los barcos en el tablero del jugador
print("""
Colocando barcos...
    """)
time.sleep(4)

#Se muestra el tablero con los barcos colocados
print("TU TABLERO")
print(tablero_legible(tablero_jugador))


time.sleep(3)

print("""
Cuando sea tu turno de atacar te mostraré una 'chuleta' como esta para 
que sepas a que coordenada pertenece cada casilla:""")

# Se muestra la chuleta de coordenadas
chuleta()

time.sleep(4)

print("""
Para atacar deberás indicar por un lado la fila a la que quieras disparar y por otro la columna.
Esto generará la coordenada donde tiraremos el misil.""")
time.sleep(3)

print("""
En el caso de acertar un barco se mostrará una X en la coordenada y podrás disparar de nuevo. 
En el caso de ser agua se revelará una triste A""")
time.sleep(2)


print("""
Por último, este es el tablero de tu oponente, Edward Thatch, en él podrás ver las casillas a las que has dispardo: """)

# Se muestra el tablero del oponente sin barcos
print(tablero_legible(ocultar_tablero(tablero_oponente)))
time.sleep(3)

print("\nComo podrás comprobar ahora mismo está en blanco asi que empecemos disparar!")

time.sleep(2)

print("\nComenzarás tu el ataque. A POR ELLO!!")

time.sleep(2)



terminar = False    # variable para finalizar el flujo cuando se gana

# Comienza el flujo con un bucle infinito que termina cuando el jugador o el ordenador gana la partida
while True:
        
    # Se imprime por pantalla la chuleta, el tablero del jugador y el tablero del ordenador sin mostrar los barcos
    print("\nTU TABLERO")
    print(tablero_legible(tablero_jugador))
    time.sleep(1)
    print("\nCHULETA DE COORDENADAS")
    chuleta()
    time.sleep(1)
    print("\nTABLERO DE EDWARD THATCH")
    print(tablero_legible(ocultar_tablero(tablero_oponente)))
    time.sleep(1)
    print("-"*100)

    
    # Turno del jugador
    while True:
        try:
            print("\nTU TURNO")
            fila = int(input("Introduce la fila a atacar (0-9): "))   # El jugador introduce una numero por teclado y se asigna a fila
            columna = int(input("Introduce la columna a atacar (0-9): "))  # El jugador introduce un numero teclado y se asigna a columna
            time.sleep(1)
            resultado = disparar((fila, columna), tablero_oponente, barcos_oponente)  # Se crea una variable resultado para mostrar al jugador el resultado de su ataque
            print(f"Disparo: ({fila}, {columna})") 
            print(tablero_legible(ocultar_tablero(tablero_oponente)))
            print("-"*100)
            if "O" not in tablero_oponente:
                print("ENOHORABUENA, HAS HUNDIDO TODOS LOS BARCOS DE EDWARD")
                terminar = True
                break     
            if resultado == "Agua" or resultado == "Repetido":  # Si el resultado es agua o coordenada repetida rompe el bucle
                break                                             

                            
            # En el caso de introducir caraacteres erroneos se pide que vuelva a introducirlos
        except (ValueError, IndexError):
            print("Coordenada erronea. Inténtalo de nuevo.")
            continue
    
    if terminar:
        break   # Si terminar es True rompe con el bucle general



            
    # Turno del ordenador
    while True:
        print("Turno de Edward...")
        time.sleep(2)
        fila, columna = turno_ordenador(tablero_jugador)      # Se generan unas coordenadas aleatorias y validas 
        resultado = disparar((fila, columna), tablero_jugador, barcos_jugador)
        print(f"Edward ha disparado a ({fila}, {columna})")
        print(tablero_legible(tablero_jugador)) # Se muestra donde ha atacado el ordenador
        print("-"*100)
        if 'O' not in tablero_jugador: # Se comprueba si quedan barcos sin hundir
            print("¡Has perdido! La máquina hundió todos tus barcos.")
            terminar = True  # Se cambia la variable terminar a True
            break
        if resultado == "Agua": # Si el resultado es agua rompe el bucle y continua con el turno del jugador
            break
    
        time.sleep(2)
    
    if terminar:   # Si terminar es True rompe con el bucle general
        break   


