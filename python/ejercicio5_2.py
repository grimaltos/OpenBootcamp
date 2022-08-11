def esprimo(numero):
    for x in range(2, numero):
        if(numero % x == 0):
            return x
            break
numerousuario = 0
while numerousuario <= 0:
    numerousuario = int(input('Por favor introduce un numero entero mayor que 0: '))
resultado = esprimo(numerousuario)
if(resultado):
    print(f'No es primo, es divisible por {resultado}')
else:
    print('Es primo')