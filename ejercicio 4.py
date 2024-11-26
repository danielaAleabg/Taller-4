##Escriba un programa que permita llenar una lista vacía por pantalla. Al llenarla ella debe ordenar los números
##contenidos y crear dos listas una para los números pares y otra para los impares.

def llenar_lista():
    lista = []
    print("Introduce los números que desees")
    print("Ingrese (fin) para terminar de escribir ")
    while True:
        entrada = input("Número: ")
        if entrada.lower() == 'fin':
            break
        try:
            numero = int(entrada)
            lista.append(numero)
        except ValueError:
            print("Por favor, introduce un número válido o 'fin' para terminar.")
    return lista

def separar_pares_impares(lista):
    lista.sort()
    pares = [num for num in lista if num % 2 == 0]
    impares = [num for num in lista if num % 2 != 0]
    return pares, impares

def main():
    """Función principal del programa."""
    lista = llenar_lista()
    print("Números ingresados" lista)
    pares, impares = separar_pares_impares(lista)
    print("Lista de números pares:", pares)
    print("Lista de números impares:", impares)

if __name__ == "__main__":
    main()

