from __future__ import annotations


class Node:
    lista_adj : list
    tipo : str

    def __init__(self, tipo: str) -> None:
        self.tipo = tipo
        lista_adj = []

    @classmethod
    def add_vizinhos(self, vizinhos : list) -> None:
        for v in vizinhos:
            self.lista_adj.extend(v)



def matrix_to_node(matrix: list) -> list:
    '''
    Recebe uma matriz lista de listas. Cada elemento é um char do mapa

    Retorna matriz lista de listas. Cada elemento é um objeto Node
    '''
    new_matrix = []

    for i in range(0,len(matrix)):
        new_line = []
        for j in range(0,len(matrix[i])):
            new_line.append(Node(tipo=matrix[i][j]))
        new_matrix.append(new_line)


    return