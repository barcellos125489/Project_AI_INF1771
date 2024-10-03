from __future__ import annotations

global meu_id
meu_id = 0

class Node:
    meu_id : int
    lista_adj : list
    tipo : str

    def __init__(self, tipo: str) -> None:
        global meu_id
        self.meu_id = meu_id
        self.tipo = tipo
        lista_adj = []

        meu_id+=1

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

def get_grafo(node_matrix : list) -> dict:
    '''
    Recebe matriz lista de listas. Cada elemento é um objeto Node

    Retorna lista de adjacencias em forma de dicionário. Chaves são os próprios nós e os valores são listas de nós adjacentes as chaves
    '''
    
    grafo = {}

    for i in range(0,len(node_matrix)):
        for j in range(0,len(node_matrix[i])):
            vizinhos = []
            
            try:
                cima = node_matrix[i][j-1] #cima
                vizinhos.append(cima)
            except:
                pass

            try:
                baixo = node_matrix[i][j+1] #baixo
                vizinhos.append(baixo)
            except:
                pass

            try:
                esquerda = node_matrix[i-1][j] #esquerda
                vizinhos.append(esquerda)
            except:
                pass
            try:
                direita = node_matrix[i+1][j] #direita
                vizinhos.append(direita)
            except:
                pass

            node_matrix[i][j].add_vizinhos(vizinhos)
            grafo[node_matrix[i][j]] = vizinhos

    return grafo
