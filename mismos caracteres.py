def contar_caracteres(palabra):
    conteo = [0] * 27 #Hay 27 letras en el alfabeto
    for caracter in palabra:
        indice = ord(caracter) - ord('a') #Ord devuelve el valor entero correspondiente al carácter en la tabla Unicode
        conteo[indice] += 1
    return conteo

def filtrar_por_caracteres(lista):
    palabras_con_mismos_caracteres = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)): #Se compara la palabra actual con las siguientes
            if contar_caracteres(lista[i]) == contar_caracteres(lista[j]):
                if lista[i] not in palabras_con_mismos_caracteres:
                    palabras_con_mismos_caracteres.append(lista[i])
                if lista[j] not in palabras_con_mismos_caracteres:
                    palabras_con_mismos_caracteres.append(lista[j])
    
    return palabras_con_mismos_caracteres

entrada = input('Ingresa una lista de palabras separadas por espacios: ')
lista_palabras = entrada.split()
palabras_con_mismos_caracteres = filtrar_por_caracteres(lista_palabras)
print("Las palabras con los mismos caracteres son:", palabras_con_mismos_caracteres)