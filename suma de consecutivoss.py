def mayor_suma_consecutiva(lista): #Se define una función para calcular la mayor suma de elementos consecutivos
    if len(lista) < 2: 
        return 'La lista debe tener al menos dos números'

    mayor_suma = lista[0] + lista[1] #Suma de los dos primeros elementos

    for i in range(1, len(lista) - 1): #Se recorre la lista desde el segundo hasta el penúltimo elemento
        suma = lista[i] + lista[i + 1]
        if suma > mayor_suma:
            mayor_suma = suma

    return mayor_suma

lista = input('Ingresa una lista de números enteros separados por espacios: ')
numeros = [int(x) for x in lista.split()]
resultado = mayor_suma_consecutiva(numeros)
print('La mayor suma entre dos elementos consecutivos es:', resultado)