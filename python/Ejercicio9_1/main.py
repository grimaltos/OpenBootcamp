listapaises = input("por favor, intoruce una lista de paises separados por una coma:\n").title().split(',')
listapaises = sorted(set(listapaises))


print(listapaises)