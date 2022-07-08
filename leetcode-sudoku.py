"""
Determine si un tablero de Sudoku de 9 x 9 es válido.
Solo las celdas llenas deben validarse de acuerdo con las siguientes reglas:

Chequear que el trablero introducido sea un tablero 9x9.
Cada fila debe contener los dígitos 1-9 sin repetición.
Cada columna debe contener los dígitos 1-9 sin repetición.
Cada uno de los nueve subcuadros de 3 x 3 de la cuadrícula debe contener los dígitos 1-9

#modularizar --> módulos: Vamos a separar en pequeñas fracciones de códigos, para ir haciendo pequeñas tareas.
Un método por regla.
"""

board = [
["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]
]

class ValidateSudoku:
    def __init__(self,tablero) -> None:
        self.tablero = tablero
        self.lista_invertida = list(), """Chequear que el tablero introducido sea un tablero 9x9"""

    def chequeo_general(self):
    #assert
        assert len(self.tablero) == 9, "El tablero ingresado no respeta el formato 9x9" #filas
        for fila in self.tablero:
         assert len(fila) == 9, "El tablero ingresado no respeta el formato 9x9"

    def chequeo_filas(self):
        for fila in self.tablero:
            for elemento in fila:
                if elemento != ".":
                    assert fila.count(elemento) ==1, "El tablero ingresado no es válido" """Esto mismo puede hacerse en una línea conteo = fila.count(elemento) if conteo > 1 --> romper"""
                    
    def chequeo_filas(self):
        for fila in self.tablero:
            for elemento in fila:
                if elemento != ".":
                    assert fila.count(elemento) ==1, "El tablero ingresado no es valido" """conteo = fila.count(elemento) if conteo > 1 --> romper - utilizamos el assert"""

                    
#instanciar el objeto
sudoku = ValidateSudoku(board)
sudoku.chequeo_general()
sudoku.chequeo_filas()


