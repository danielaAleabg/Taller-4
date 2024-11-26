##Diseñe un algoritmo que le permita crear una lista con
##nombres de estudiantes (N nombres), su programa debe permitir
##buscar si los nombres están contenidos en la lista, la consulta
##solicita nombres y verifica si están o no.

lista_estudiantes = []

def agregar():
    global lista_estudiantes
    
    n = int(input("¿Cuántos nombres de estudiantes deseas ingresar? "))
    
    for i in range(n):
        nombre = input(f"Ingresa el nombre del estudiante {i+1}: ")
        lista_estudiantes.append(nombre)
    
    print("\n¡Lista de estudiantes registrada con éxito!")

def consultar():
    consulta = input("\nIngresa el nombre del estudiante que deseas buscar: ")
    
    if consulta in lista_estudiantes:
        print(f"El estudiante '{consulta}' está en la lista.")
    else:
        print(f"El estudiante '{consulta}' no está en la lista.")
def main():
    while True:
        print("_____MENÚ____")
        print("1. Ingresar estudiante.")
        print("2. Buscar estudiante.")

        
        opcion = input("¿Qué desea hacer?: ")
        
        if opcion == "1":
            agregar()
        elif opcion == "2":
            consultar()  
        else:
            print("ERROR... Opción no válida")

if __name__ == "__main__":
    main()
