listapaises = input("por favor, intoruce una lista de paises separados por una coma:\n").split(',')
listapaises = sorted(set(listapaises))


print(",".join(listapaises))