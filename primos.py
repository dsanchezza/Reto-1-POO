def es_primo(numero): #Se define una función para verificar si un número es primo
    if numero < 2: 
        return False
    for i in range(2, int(numero ** 0.5) + 1): #Se comprueban divisores desde 2 hasta la raíz cuadrada del numero
        if numero % i == 0: #Si el número es divisible por 'i', no es primo
            return False
    return True

def filtrar_primos(lista): #Se define una función que recibe una lista de números
    primos = [] 
    for num in lista:  
        if es_primo(num): #Si el número es primo, se añade a la lista de primos
            primos.append(num)
    return primos

lista = input("Ingresa una lista de números separados por espacios: ")
numeros = [int(x) for x in lista.split()]
primos = filtrar_primos(numeros)
print("Los números primos son:", primos)