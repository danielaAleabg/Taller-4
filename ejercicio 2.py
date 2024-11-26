meses = (
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
)

while True:
    try:
        numero = int(input("Ingrese un número entre 1-12 (o 0 para salir): "))

        if numero == 0:
            print("SALIENDO...")
            break
        if 1 <= numero <= len(meses):
            print(f"El mes correspondiente es: {meses[numero - 1]}.")
        else:
            print("Error: el número ingresado no está en el rango permitido.")
    except ValueError:
        print("Error: por favor ingrese un número válido.")
