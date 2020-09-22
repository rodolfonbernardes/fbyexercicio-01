# -*- coding: utf-8 -*-

# Pilhas são estruturas de dados em que só é possível inserir um novo elemento no final
# da pilha e só é possível remover um elemento do final da pilha. Em Python utilizamos
# listas como se fossem pilhas. O último elemento a ser inserido é sempre o primeiro
# elemento a ser removido.

from collections import deque
pilha = [1, 1, 12, 3, 5]
#print(f'Pilha: {pilha}')

pilha.append(8)
#print(f'Inserindo um elemento: {pilha}')

pilha.pop()
#print(f'Removendo um elemento: {pilha}')

# Implementando uma pilha como estrutura encadeada. A pilha possui um topo e cada elemento
# faz referência ao elemento anterior.

class Nodo:
    """Esta classe representa um nodo de uma estrutura encadeada."""

    def __init__(self, dado=0, nodo_anterior=None):
        self.dado = dado
        self.anterior = nodo_anterior

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.anterior)

class Pilha:
    """Esta classe representa uma pilha usando uma estrutura encadeada."""

    def __init__(self):
        self.topo = None

    def __repr__(self):
        return "[" + str(self.topo) + "]"

    def insere(self, novo_dado):
        """Insere um elemento no final da fila"""

        # Cria um novo nodo com o dado a ser armazenado
        novo_nodo = Nodo(novo_dado)

        # Faz com que o novo nodo seja o topo da pilha
        novo_nodo.anterior = self.topo

        # Faz com que a cabeça da lista referencie o novo nodo
        self.topo = novo_nodo

    def remove(self):
        """Remove o elemento que está no topo da pilha."""

        assert self.topo, "Impossível remover valor de pilha vazia."

        self.topo = self.topo.anterior

# Cria uma pilha vazia
pilha = Pilha()
#print(f'Pilha vazia" {pilha}')

# Insere elementos na pilha
for i in range(5):
    pilha.insere(i)
    #print("Insere o valor {0} no topo da pilha: {1}".format(i, pilha))

while pilha.topo != None:
    pilha.remove()
    #print("Removendo elemento que está no topo da pilha: ", pilha)

