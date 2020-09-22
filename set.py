# -*- coding: utf-8 -*-

# Set: uma coleção de dados não ordenada e não indexada

# função para imprimir itens
def print_set(set_to_be_printed):
    for item in set_to_be_printed:
        print(item)
    print("Tamanho da set:",len(set_to_be_printed),"itens")

# Exemplo de criação 
my_set = {"Mateus","Marcos","Lucas","João"}
print("Set original")
print_set(my_set)

# Inclusão de itens
my_set.add("Paulo")
print("Set com mais um item")
print_set(my_set)

# Remoção de itens
my_set.remove("Marcos")
print("Set com menos um item")
print_set(my_set)