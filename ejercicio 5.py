##Escribir una función sumar() y una función multiplicar(),
##estas deben sumar y multiplicar respectivamente todos
##los números de una lista. #Por ejemplo: sumar([1,2,3,4])
##debería devolver 10 y multiplicar([1,2,3,4]) debería
##devolver 24.
def sumar():
    return sum(lista)

def multiplicar():
    resultado = 1
    for numero in lista:
        resultado *= numero
    return resultado


numeros = input("Ingrese los números que desea sumar y multiplicar, estos deben esar separados por una coma: ")
lista= [int(numero) for numero in numeros.split(",")]
print(f"La suma de {lista} es: {sumar()}")  
print(f"El producto de {lista} es: {multiplicar()}")  
