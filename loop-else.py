# -*- coding: utf-8 -*-

# loop-else: O statement else quando usado em um loop trata o retorno false da condicão estabelecida dentro do for. 

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')
