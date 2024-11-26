libros = {
    '978-3-16-148410-0': {'titulo': 'Cien años de soledad', 'autor': 'Gabriel García Márquez', 'año': 1967, 'referencia': 'L001'},
    '978-0-7432-7356-5': {'titulo': 'El alquimista', 'autor': 'Paulo Coelho', 'año': 1988, 'referencia': 'L002'},
    '978-0-06-112241-5': {'titulo': 'Harry Potter y la piedra filosofal', 'autor': 'J.K. Rowling', 'año': 1997, 'referencia': 'L003'},
    '978-1-4028-9462-6': {'titulo': '1984', 'autor': 'George Orwell', 'año': 1949, 'referencia': 'L004'},
    '978-1-59308-201-3': {'titulo': 'Orgullo y prejuicio', 'autor': 'Jane Austen', 'año': 1813, 'referencia': 'L005'}
}

usuarios = {}
consultas_libros = 0  

def mostrar_libros():
    print("\n--- Libros disponibles ---")
    for libro in libros.values():
        print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Año: {libro['año']}, Referencia: {libro['referencia']}")

def consultar_libro():
    global consultas_libros
    opcion = input("\n¿Cómo desea consultar el libro?\n1. Por título\n2. Por autor\nSeleccione una opción (1-2): ")
    
    if opcion == '1':
        titulo = input("Ingrese el título del libro que desea consultar: ").lower()
        encontrado = False
        for libro in libros.values():
            if titulo in libro['titulo'].lower():
                print(f"\nLibro encontrado: Título: {libro['titulo']}, Autor: {libro['autor']}, Año: {libro['año']}, Referencia: {libro['referencia']}")
                consultas_libros += 1
                encontrado = True
        if not encontrado:
            print(f"No se encontró ningún libro con el título '{titulo}'.")
    
    elif opcion == '2':
        autor = input("Ingrese el autor del libro que desea consultar: ").lower()
        encontrado = False
        for libro in libros.values():
            if autor in libro['autor'].lower():
                print(f"\nLibro encontrado: Título: {libro['titulo']}, Autor: {libro['autor']}, Año: {libro['año']}, Referencia: {libro['referencia']}")
                consultas_libros += 1
                encontrado = True
        if not encontrado:
            print(f"No se encontró ningún libro de autor '{autor}'.")
    
    else:
        print("Opción no válida.")

def agregar_libro():
    if len(libros) >= 5:
        print("\nNo se pueden agregar más libros. El inventario está completo.")
        return
    
    isbn = input("\nIngrese el ISBN del nuevo libro: ")
    if isbn in libros:
        print("Este libro ya existe en el inventario.")
        return
    
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    año = input("Ingrese el año de publicación: ")
    referencia = input("Ingrese el número de referencia: ")
    
    libros[isbn] = {'titulo': titulo, 'autor': autor, 'año': int(año), 'referencia': referencia}
    print(f"\nEl libro '{titulo}' ha sido agregado al inventario.")

def registrar_usuario():
    nombre = input("\nIngrese el nombre del nuevo usuario: ")
    if nombre in usuarios:
        print("Este usuario ya está registrado.")
    else:
        usuarios[nombre] = {'nombre': nombre}
        print(f"Usuario '{nombre}' registrado con éxito.")

def mostrar_estadisticas():
    print("\n--- Estadísticas ---")
    print(f"Total de usuarios registrados: {len(usuarios)}")
    print(f"Total de consultas de libros: {consultas_libros}")

def menu():
    while True:
        print("\n--- Menú de la Biblioteca ---")
        print("1. Mostrar todos los libros")
        print("2. Consultar un libro")
        print("3. Agregar un nuevo libro")
        print("4. Registrar un nuevo usuario")
        print("5. Mostrar estadísticas")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            mostrar_libros()
        elif opcion == '2':
            consultar_libro()
        elif opcion == '3':
            agregar_libro()
        elif opcion == '4':
            registrar_usuario()
        elif opcion == '5':
            mostrar_estadisticas()
        elif opcion == '6':
            print("\nGracias por usar el sistema de la biblioteca. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == '__main__':
    menu()
