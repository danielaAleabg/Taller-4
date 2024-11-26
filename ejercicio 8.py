def mostrar_agenda(agenda):
    """Muestra todos los contactos de la agenda."""
    if len(agenda) == 0:
        print("La agenda está vacía.")
    else:
        print("\nAgenda Telefónica:")
        for nombre, datos in agenda.items():
            print(f"Nombre: {nombre}")
            print(f"Teléfono: {datos['telefono']}")
            print(f"Correo: {datos['correo']}")
            print(f"Dirección: {datos['direccion']}")
            print(f"Cumpleaños: {datos['cumpleaños']}\n")

def agregar_contacto(agenda):
    """Agrega un nuevo contacto a la agenda."""
    nombre = input("Ingrese el nombre completo (Nombre y Apellido): ")
    telefono = input("Ingrese el número de teléfono: ")
    correo = input("Ingrese el correo electrónico: ")
    direccion = input("Ingrese la dirección de residencia: ")
    cumpleaños = input("Ingrese el cumpleaños (formato: dd/mm/aaaa): ")
    
    agenda[nombre] = {
        'telefono': telefono,
        'correo': correo,
        'direccion': direccion,
        'cumpleaños': cumpleaños
    }
    print(f"Contacto {nombre} agregado correctamente.\n")

def editar_contacto(agenda):
    """Edita la información de un contacto existente."""
    nombre = input("Ingrese el nombre del contacto a editar: ")
    if nombre in agenda:
        print(f"Editando contacto de {nombre}")
        telefono = input(f"Ingrese el nuevo teléfono (actual: {agenda[nombre]['telefono']}): ")
        correo = input(f"Ingrese el nuevo correo (actual: {agenda[nombre]['correo']}): ")
        direccion = input(f"Ingrese la nueva dirección (actual: {agenda[nombre]['direccion']}): ")
        cumpleaños = input(f"Ingrese el nuevo cumpleaños (actual: {agenda[nombre]['cumpleaños']}): ")
        
        agenda[nombre] = {
            'telefono': telefono,
            'correo': correo,
            'direccion': direccion,
            'cumpleaños': cumpleaños
        }
        print(f"Contacto {nombre} actualizado correctamente.\n")
    else:
        print("El contacto no existe en la agenda.\n")

def eliminar_contacto(agenda):
    """Elimina un contacto de la agenda."""
    nombre = input("Ingrese el nombre del contacto a eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} eliminado correctamente.\n")
    else:
        print("El contacto no existe en la agenda.\n")

def main():
    agenda = {}
    
    while True:
        print("---- Menú de la Agenda Telefónica ----")
        print("1. Agregar contacto")
        print("2. Editar contacto")
        print("3. Eliminar contacto")
        print("4. Mostrar agenda")
        print("5. Salir")
        
        opcion = input("Elija una opción: ")
        
        if opcion == '1':
            agregar_contacto(agenda)
        elif opcion == '2':
            editar_contacto(agenda)
        elif opcion == '3':
            eliminar_contacto(agenda)
        elif opcion == '4':
            mostrar_agenda(agenda)
        elif opcion == '5':
            print(f"Total de contactos en la agenda: {len(agenda)}")
            for nombre in agenda:
                print(f"Nombre: {nombre}")
            print("SALIENDO...")
            break
        else:
            print("Opción no válida. Por favor, elija una opción entre 1 y 5.\n")

if __name__ == "__main__":
    main()
