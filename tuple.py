
# -*- coding: utf-8 -*-

# Tuplas são parecidas com listas, mas tuplas são imutáveis:
# uma vez que você cria uma tupla, você não pode modificá-la
# de nenhuma forma, ou seja, não pode alterar um elemento da
# tupla, não pode inserir elementos, e não pode remover elementos.

# Exemplo função para imprimir itens
def print_tuple(tuple_to_be_printed):
    for item in tuple_to_be_printed:
        print(item)
    print("Tamanho da tuple:",len(tuple_to_be_printed),"itens")

# Exemplo de criação de tuplas.
tupla_vazia = () # Também é possível fazer: tupla_vazia = tuple()
print("Tupla vazia: ", tupla_vazia)

coordenada = (10, 20)
print("Exemplo de tupla: ", coordenada)

print("Tipo de uma tupla: ", type(coordenada))

lat, long = 31.79, 56.14
print("Outro exemplo de criação de tupla: ", (lat, long))

# primeiro item da tupple
print("Primeiro item da tuple:",my_tuple[0])
print("#########################")

# último item da tupple
print("Último item da tuple:",my_tuple[-1])
print("#########################")