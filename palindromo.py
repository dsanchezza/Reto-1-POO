def ingresar_palabra(): #Se define una función para ingresar la palabra
    palabra = input('Ingresa una palabra: ') 
    return palabra

def es_palindromo(palabra): #Se define una función para verificar si la palabra es un palíndromo
    inicio = 0 #Comenzar desde el primer carácter de la palabra
    fin = len(palabra) - 1 #Comenzar desde el último carácter de la palabra
    
    while inicio < fin:
        if palabra[inicio] != palabra[fin]: #Si los caracteres en las posiciones 'inicio' y 'fin' no son iguales
            return False #No es un palíndromo
        inicio += 1 
        fin -= 1
    
    return True #Si todos los pares de caracteres son iguales, es un palíndromo

palabra = ingresar_palabra()

if es_palindromo(palabra):
    print(f'La palabra "{palabra}" es un palíndromo.')
else:
    print(f'La palabra "{palabra}" no es un palíndromo.')