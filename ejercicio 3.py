personas = [
    {"nombre": "María",
     "direccion": "cra 3",
     "telefono": "123456789"},
    {"nombre": "Juan",
     "direccion": " 456",
     "telefono": "987654321"},
    {"nombre": "German",
     "direccion": "vereda tubabita ",
     "telefono": "567890123"}
]

def mostrar_personas():
    print("\nLista de personas:")
    for i, persona in enumerate(personas):
        print(f"{i + 1}. Nombre: {persona['nombre']}, Dirección: {persona['direccion']}, Teléfono: {persona['telefono']}")

while True:
    try:
        mostrar_personas()

        opcion = int(input("\nIngrese el número de la persona que desea editar (o 0 para salir): "))
        if opcion == 0:
            print("Programa terminado.")
            break
        if 1 <= opcion <= len(personas):
            persona_seleccionada = personas[opcion - 1]
            print(f"Editando a: {{persona_seleccionada['nombre']}")
            nueva_direccion = input("Ingrese la nueva dirección: ")
            nuevo_telefono = input("Ingrese el nuevo teléfono: ")
            persona_seleccionada['direccion'] = nueva_direccion
            persona_seleccionada['telefono'] = nuevo_telefono

            print("Datos actualizados correctamente.")
        else:
            print("Error: el número ingresado no está en el rango permitido.")
    except ValueError:
        print("Error: por favor ingrese un número válido.")
