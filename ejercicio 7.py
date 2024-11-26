##Aplicando los diccionarios, elabore un traductor que permita
##al usuario por pantalla seleccionar el idioma y buscar palabras.
##También debe permitir agregar palabras nuevas y borrar palabras
##con errores. Por ejemplo: Introduciremos una palabra en español y
##la "traducirá" a ingles. Para ello tendrás que introducir un diccionario
##de palabras (al menos 10 palabras ). Al ejecutar el programa este debe
##permitir ver el significado de las palabras y agregar las que no se
##encuentren en él (es decir se solicita una palabra que no esta en el
##diccionario, este debe informar que la palabra no esta registrada en
##la base de datos y permitir su ingreso). Además de poder eliminar algunas
##de las ya incluidas o editar las que estén mal escritas.
##traductor = {'auto': 'car', 'azul': 'blue', 'red': 'rojo', 'volar':
##'fly', 'blanco': 'white', 'casa': 'house','clase': 'class', 'futbol': 'soccer', 'hora': 'hour', 'cama': 'bathroom'}

def menu():
    print("\n--- Traductor ---")
    print("1. Traducir una palabra")
    print("2. Agregar una palabra nueva")
    print("3. Editar una palabra")
    print("4. Eliminar una palabra")
    print("5. Mostrar todas las palabras")
    print("6. Salir")

def ingles():
    print("\n--- Traductor Español-Inglés ---")
    traductor = {
        'auto': 'car',
        'azul': 'blue',
        'rojo': 'red',
        'volar': 'fly',
        'blanco': 'white',
        'casa': 'house',
        'clase': 'class',
        'futbol': 'soccer',
        'hora': 'hour',
        'cama': 'bed'
    }

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            palabra = input("Ingrese la palabra en español que desea traducir: ").lower()
            if palabra in traductor:
                print(f"La traducción de '{palabra}' es '{traductor[palabra]}'.")
            else:
                print(f"La palabra '{palabra}' no está en el diccionario.")

        elif opcion == '2':
            palabra = input("Ingrese la palabra en español que desea agregar: ").lower()
            if palabra in traductor:
                print(f"La palabra '{palabra}' ya está en el diccionario.")
            else:
                traduccion = input(f"Ingrese la traducción de '{palabra}' en inglés: ").lower()
                traductor[palabra] = traduccion
                print(f"La palabra '{palabra}' con traducción '{traduccion}' fue agregada.")

        elif opcion == '3':
            palabra = input("Ingrese la palabra en español que desea editar: ").lower()
            if palabra in traductor:
                nueva_traduccion = input(f"Ingrese la nueva traducción para '{palabra}': ").lower()
                traductor[palabra] = nueva_traduccion
                print(f"La palabra '{palabra}' fue actualizada con la traducción '{nueva_traduccion}'.")
            else:
                print(f"La palabra '{palabra}' no está en el diccionario.")

        elif opcion == '4':
            palabra = input("Ingrese la palabra en español que desea eliminar: ").lower()
            if palabra in traductor:
                del traductor[palabra]
                print(f"La palabra '{palabra}' fue eliminada del diccionario.")
            else:
                print(f"La palabra '{palabra}' no está en el diccionario.")

        elif opcion == '5':
            if traductor:
                print("\nPalabras en el diccionario:")
                for esp, eng in traductor.items():
                    print(f"{esp} -> {eng}")
            else:
                print("El diccionario está vacío.")

        elif opcion == '6':
            print("Saliendo del traductor. ¡Hasta pronto!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

def portugues():
    print("\n--- Traductor Español-Portugués ---")
    traductor_portugues = {
        'auto': 'carro',
        'azul': 'azul',
        'rojo': 'vermelho',
        'volar': 'voar',
        'blanco': 'branco',
        'casa': 'casa',
        'clase': 'classe',
        'futbol': 'futebol',
        'hora': 'hora',
        'cama': 'cama',
        'libro': 'livro',
        'escuela': 'escola',
        'comer': 'comer',
        'caminar': 'andar',
        'feliz': 'feliz',
        'familia': 'família',
        'trabajo': 'trabalho',
        'agua': 'água',
        'pan': 'pão'
    }

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            palabra = input("Ingrese la palabra en español que desea traducir: ").lower()
            if palabra in traductor_portugues:
                print(f"La traducción de '{palabra}' es '{traductor_portugues[palabra]}'.")
            else:
                print(f"La palabra '{palabra}' no está en el diccionario.")

        elif opcion == '2':
            palabra = input("Ingrese la palabra en español que desea agregar: ").lower()
            if palabra in traductor_portugues:
                print(f"La palabra '{palabra}' ya está en el diccionario.")
            else:
                traduccion = input(f"Ingrese la traducción de '{palabra}' en portugués: ").lower()
                traductor_portugues[palabra] = traduccion
                print(f"La palabra '{palabra}' con traducción '{traduccion}' fue agregada.")

        elif opcion == '3':
            palabra = input("Ingrese la palabra en español que desea editar: ").lower()
            if palabra in traductor_portugues:
                nueva_traduccion = input(f"Ingrese la nueva traducción para '{palabra}': ").lower()
                traductor_portugues[palabra] = nueva_traduccion
                print(f"La palabra '{palabra}' fue actualizada con la traducción '{nueva_traduccion}'.")
            else:
                print(f"La palabra '{palabra}' no está en el diccionario.")

        elif opcion == '4':
            palabra = input("Ingrese la palabra en español que desea eliminar: ").lower()
            if palabra in traductor_portugues:
                del traductor_portugues[palabra]
                print(f"La palabra '{palabra}' fue eliminada del diccionario.")
            else:
                print(f"La palabra '{palabra}' no está en el diccionario.")

        elif opcion == '5':
            if traductor_portugues:
                print("\nPalabras en el diccionario:")
                for esp, por in traductor_portugues.items():
                    print(f"{esp} -> {por}")
            else:
                print("El diccionario está vacío.")

        elif opcion == '6':
            print("Saliendo del traductor. ¡Hasta pronto!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

def frances():
    print("\n--- Traductor Español-Francés ---")
    traductor_frances = {
        'auto': 'voiture',
        'azul': 'bleu',
        'rojo': 'rouge',
        'volar': 'voler',
        'blanco': 'blanc',
        'casa': 'maison',
        'clase': 'classe',
        'futbol': 'football',
        'hora': 'heure',
        'cama': 'lit',
        'libro': 'livre',
        'escuela': 'école',
        'comer': 'manger',
        'caminar': 'marcher',
        'feliz': 'heureux',
        'familia': 'famille',
        'trabajo': 'travail',
        'agua': 'eau',
        'pan': 'pain'
    }

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            palabra = input("Ingrese la palabra en español que desea traducir: ").lower()
            if palabra in traductor_frances:
                print(f"La traducción de '{palabra}' es '{traductor_frances[palabra]}'.")
            else:
                print(f"La palabra '{palabra}' no está en el diccionario.")

        elif opcion == '2':
            palabra = input("Ingrese la palabra en español que desea agregar: ").lower()
            if palabra in traductor_frances:
                print(f"La palabra '{palabra}' ya está en el diccionario.")
            else:
                traduccion = input(f"Ingrese la traducción de '{palabra}' en francés: ").lower()
                traductor_frances[palabra] = traduccion
                print(f"La palabra '{palabra}' con traducción '{traduccion}' fue agregada.")

        elif opcion == '3':
            palabra = input("Ingrese la palabra en español que desea editar: ").lower()
            if palabra in traductor_frances:
                nueva_traduccion = input(f"Ingrese la nueva traducción para '{palabra}': ").lower()
                traductor_frances[palabra] = nueva_traduccion
                print(f"La palabra '{palabra}' fue actualizada con la traducción '{nueva_traduccion}'.")
            else:
                print(f"La palabra '{palabra}' no está en el diccionario.")

        elif opcion == '4':
            palabra = input("Ingrese la palabra en español que desea eliminar: ").lower()
            if palabra in traductor_frances:
                del traductor_frances[palabra]
                print(f"La palabra '{palabra}' fue eliminada del diccionario.")
            else:
                print(f"La palabra '{palabra}' no está en el diccionario.")

        elif opcion == '5':
            if traductor_frances:
                print("\nPalabras en el diccionario:")
                for esp, fra in traductor_frances.items():
                    print(f"{esp} -> {fra}")
            else:
                print("El diccionario está vacío.")

        elif opcion == '6':
            print("Saliendo del traductor. ¡Hasta pronto!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

def main():
    while True:
        print("\nSeleccione el idioma del traductor:")
        print("1. Español-Inglés")
        print("2. Español-Portugués")
        print("3. Español-Francés")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            ingles()
        elif opcion == '2':
            portugues()
        elif opcion == '3':
            frances()
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == '__main__':
    main()

