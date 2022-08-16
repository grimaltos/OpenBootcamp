from functools import reduce

numeros = input("por favor, intoruce una lista numeros enteros:\n")
listanumeros = [int(numero) for numero in numeros.split(',')]
print(listanumeros)
listanumeros = list(filter(lambda x: x %2 ,listanumeros))
print(listanumeros)
listanumeros = reduce((lambda x, y: x + y), listanumeros)
print(listanumeros)


