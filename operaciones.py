def ingresar_operacion():  #Se define una función para ingresar la operación
    operación = input('Ingresa una operación: ')
    if operación not in ['+', '-', '*', '/']: #Si la operación no es una de las básicas, se le pedirá a la persona que ingrese una válida
        print('Ingresa una operación válida')
        return None #Si la operación no es válida el programa se cerrará
    else:
        return operación 
    
operación = ingresar_operacion()

if operación: #El programa solo continúa si la operación es válida
    numero1 = int(input('Ingresa el primer numero: '))
    numero2 = int(input('Ingresa el segundo numero: '))
    if operación == '+':
        print(f'El resultado de la suma es: {numero1 + numero2}')
    elif operación == '-':
        print(f'El resultado de la resta es: {numero1 - numero2}')
    elif operación == '*':
        print(f'El resultado de la multiplicación es: {numero1 * numero2}')
    elif operación == '/':
        print(f'El resultado de la división es: {numero1 / numero2}')