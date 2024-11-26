registro1 = [
    ("María", "Garzón", "1101753473", "Calle 8-39, Bogotá", "3246762838"),
    ("Carlos", "Pérez", "63433981", "Carrera 3, Bucaramanga", "3003746010"),
    ("Edith", "Martínez", "79432172", "Vereda Tubabita, Velez-Santander", "3227489331")
]

def mostrar_base_datos(base_datos):
    print("Nombre      Apellido    Documento       Dirección               Teléfono")
    print("-" * 65)
    for registro in base_datos:
        print(f"{registro[0]:<12}{registro[1]:<12}{registro[2]:<15}{registro[3]:<22}{registro[4]}")

def agregar_registro(base_datos, registro):
    base_datos.append(registro)

def buscar_por_documento(base_datos, documento):
    return next((registro for registro in base_datos if registro[2] == documento), None)

print("Base de datos inicial:")
mostrar_base_datos(registro1)

nuevo_registro = ("María", "López", "112233445", "Diagonal 20, Cartagena", "3001122334")
agregar_registro(registro1, nuevo_registro)

print("\nBase de datos actualizada:")
mostrar_base_datos(registro1)
print("-"*68)
print("Ingrese el documento que desea encontrar: ")
doc = "456789123"
print(doc)
print(f"\nBuscando documento {doc}.........")
registro = buscar_por_documento(registro1, doc)
print(f"Registro encontrado: {registro}" if registro else "No se encontró el registro.")
