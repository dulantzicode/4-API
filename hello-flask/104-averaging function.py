from os import system
system('cls')

from functools import reduce

def get_average(list):
    total = reduce((lambda total, element: total + element), list)
    return total / len(list)


avg = get_average([1, 2, 3, 4, 5, 6])

print(avg)


#alternativa 1

import statistics

list_1=[1,2,3,4,5,6,7,8,9]

print(statistics.mean(list_1))



#alternativa 2

import numpy

list_1=[1,2,3,4,5,6,7,8,9]

print(numpy.mean(list_1))





#ejercicio
def media(list):
    long= len(list)
    total = 0
    for valor in list:
        total += valor
    return total/long

valor_medio = media([50,50,5,7,9,11,45,50,50,1])

print (valor_medio)