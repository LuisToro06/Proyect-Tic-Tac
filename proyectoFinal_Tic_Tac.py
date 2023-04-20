from random import randrange

def mostrar_tablero(board):
    print("+-------" * 3,"+", sep="")
    for row in range(3):
        print("|       " * 3,"|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3,"|", sep="")
        print("+-------" * 3,"+", sep="")
print("Algun cambió")
def movimiento(board):
    okay = False
    while not okay:
        mover = input("Digite el movimiento: ")
        okay = len(mover) == 1  and mover >= '1' and mover <= '9' # con el len se verifica un solo dígito y es verdadero o falso y lo compara con el rango entre 1 a 9
        #print("Entra o No", okay)
        if not okay:
            print("Movimiento erróneo, ingrésalo de nuevo: ")
            continue
        #print("Entra o No")
        mover = int(mover) - 1 # número de celda del 0 a 8
        fila = mover // 3
        columna = mover % 3
        marcado = board[fila][columna]
        #print(marcado)
        okay = marcado not in ["O","X"]# verifico que está el espacio
        #print("valor", okay)
        if not okay: # indica que está el espacio ocupado por ["O", "X"]
            print("Cuadro ocupado, Ingrese un nuevo valor:")
            continue
    board[fila][columna] = 'O' # se le asigna el valor del humano

def lista_campos_disponibes(board):
    free = []
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ["O", "X"]: # celda libre
                free.append((i, j)) # obtengo una lista con los espacios libre
    return free # retorno los espacios libre de las celdas en listas

def victoria_para(board,ficha):
    if ficha == 'X':
        quines = 'maq'
    elif ficha == 'O':
        quines = 'hum'
        print("Por aquí",quines)
    else: 
        quines = None
    cruz1 = cruz2 = True
    for rev in range(3):
        if board[rev][0] == ficha and board[rev][1] == ficha and board[rev][2] == ficha:
            return quines
        if board[0][rev] == ficha and board[1][rev] == ficha and board[2][rev] == ficha:
            return quines
        if board[rev][rev] != ficha:
            cruz1 = False
        if board[2 - rev][2 - rev] != ficha:
            cruz2 = False
    if cruz1 or cruz2:
        return quines
    return None        
        
def dibujo_maquina(board):
    disponible = lista_campos_disponibes(board)
    contar = len(disponible)
    if contar > 0: #"Si no está vacío" 
        this = randrange(contar)
        fila, columna = disponible[this] # me devuelve un valor en forma de lista, tomo un ítem de 
         # de ella (0, 2), entonces a fila le asigno el valor de 0 y columna el valor de 2
        board[fila][columna] = 'X'       


# Se empieza por aquí...
board = [[3*i + j + 1 for j in range (3)] for i in range (3)]
#print (board)
board[1][1] = "X"
#print(board)
disponible = lista_campos_disponibes(board) # obtenga la lista de las celdas libre
#print(len(disponible))
humano = True # el turno
while len(disponible): # condicion si está lleno es True, en caso contrario Falso
    mostrar_tablero(board)

    #print(mostrar_tablero)
    if humano:
        movimiento(board)
        victoria = victoria_para(board,'O')
        print("Hola", victoria)
    else: 
        dibujo_maquina(board)
        victoria = victoria_para(board,'X')
        print("Máquina",victoria)
    if victoria != None:
        print("Cuando aquí")
        break 
    humano = not humano # se vuelve falso, luego entra la máquina y luego se vuelve True y así sucesivamente
    print("juego humano", humano)
    disponible = lista_campos_disponibes(board)
    print("Nuevo", disponible)

   
mostrar_tablero(board)
#print("por aquí mostrando")
if victoria  == 'hum':
    print("¡Haz ganado!") 
elif victoria  == 'maq':
    print("He ganado")  
else:
    print("Empate técnico")
#print(disponible)
#mostrar_tablero(board)