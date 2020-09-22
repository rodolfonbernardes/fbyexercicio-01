# -*- coding: utf-8 -*-

# Filas são estruturas de dados em que só é possível inserir um novo elemento no final da
# fila e só é possível remover um elemento do início. Filas seguem um protocolo em que o 
# primeiro a entrar é o primeiro a sair. Podemos implementar fiilas usando listas e a
# biblioteca deque.

fila = deque(["Eric", "John", "Michael"])
fila.append("Terry")  # Terry Chega
fila.append("Graham")  # Graham chega
fila.popleft()  # O primeiro a chegar parte [Eric]
fila.popleft()  # O segundo a chegar parte [John]
# print(fila) ## O resto da fila, em ordem de chegada

# Implementando filas com estruturas encadeadas. Inserções ocorrem no final da fila e remoções
# ocorrem no começo. São dois ponteiros: um para o começo da fila e outro para o final. Eses
# ponteiros permitem inserções e remoções com custo constante.

class Nodo:
    #Esta classe representa um nodo de uma estrutura duplamente encadeada.

    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)

class Fila:
    #Esta classe representa uma fila usando uma estrutura encadeada.

    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __repr__(self):
        return "[" + str(self.primeiro) + "]"

    def insere(self, novo_dado):
        """Insere um elemento no final da fila."""

        # Cria um novo nodo com o dado a ser armazenado
        novo_nodo = Nodo(novo_dado)

        # Insere em uma fila vazia
        if self.primeiro == None:
            self.primeiro = novo_nodo
            self.ultimo = novo_nodo
        else:
            # Faz com que o novo nodo seja o último da fila.
            self.ultimo.proximo = novo_nodo

            # Faz com que o último da fila referencie o novo nodo.
            self.ultimo = novo_nodo

    def remove(self):
        #Remove o último elemento da fila"""

        assert self.primeiro != None, "Impossível remover elemento de fila vazia"

        self.primeiro = self.primeiro.proximo

        if(self.primeiro) == None:
            self.ultimo = None

fila = Fila()
#print("Fila vazia: ", fila)

# Insere elementos na fila
for i in range(5):
    fila.insere(i)
    #print("Insere o valor {0} no final da fila: {1}".format(i, fila))

while fila.primeiro != None:
    fila.remove()
    #print("Removendo elemento que está no começo da fila: ", fila)