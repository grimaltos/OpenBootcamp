edad = int(input('Por favor introduzca su edad: '))
if(edad < 0):
    print('Por favor introduzca una edad válida')
elif(edad < 18):
    print('Es usted menor de edad')
else:
    print('Es usted mayor de edad')