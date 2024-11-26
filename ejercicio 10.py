import time

parqueadero = {}

precio_moto = 2000  
precio_carro = 5000  

contador_motos = 0
contador_carros = 0
dinero_recaudado = 0

def generar_codigo():
    """Genera un código aleatorio de 5 dígitos para los vehículos."""
    return str(int(time.time()) % 100000)

def registrar_vehiculo(tipo):
    """Registra un vehículo (moto o carro) en el parqueadero."""
    global contador_motos, contador_carros
    codigo = generar_codigo()
    hora_ingreso = time.time()
    parqueadero[codigo] = {'tipo': tipo, 'hora_ingreso': hora_ingreso}
    
    if tipo == "moto":
        contador_motos += 1
    elif tipo == "carro":
        contador_carros += 1
    
    print(f"Vehículo registrado. Código asignado: {codigo}")
    
def calcular_tiempo_estacionado(codigo):
    """Calcula el tiempo de parqueo en horas (fracción de hora redondeada)."""
    hora_salida = time.time()
    hora_ingreso = parqueadero[codigo]['hora_ingreso']
    tiempo_en_segundos = hora_salida - hora_ingreso
    tiempo_en_horas = (tiempo_en_segundos / 3600)  
    return round(tiempo_en_horas, 2)  

def cobrar_salida(codigo):
    """Realiza el cobro a la salida del parqueadero."""
    if codigo not in parqueadero:
        print("Código no encontrado.")
        return
    
    tipo_vehiculo = parqueadero[codigo]['tipo']
    tiempo_estacionado = calcular_tiempo_estacionado(codigo)
    
    if tipo_vehiculo == "moto":
        costo = tiempo_estacionado * precio_moto
    else: 
        costo = tiempo_estacionado * precio_carro
    
    global dinero_recaudado
    dinero_recaudado += costo
    
    print(f"Tiempo estacionado: {tiempo_estacionado} horas")
    print(f"Cobro total: {costo} COP")
    
    pago = float(input("Ingrese el monto recibido: "))
    
    while pago < costo:
        print("Monto insuficiente. Intente de nuevo.")
        pago = float(input("Ingrese el monto recibido: "))
    
    vuelto = pago - costo
    if vuelto > 0:
        print(f"Vuelto: {vuelto} COP")
    print("Gracias por usar nuestro parqueadero.")
    del parqueadero[codigo]

def mostrar_estadisticas():
    """Muestra las estadísticas del día."""
    global dinero_recaudado
    print("\n--- Estadísticas del Parqueadero ---")
    print(f"Total de motos ingresadas: {contador_motos}")
    print(f"Total de carros ingresados: {contador_carros}")
    print(f"Dinero recaudado: {dinero_recaudado} COP")

def menu():
    """Interfaz de usuario para operar el parqueadero."""
    while True:
        print("\n--- Menú del Parqueadero ---")
        print("1. Registrar moto")
        print("2. Registrar carro")
        print("3. Cobrar salida")
        print("4. Mostrar estadísticas")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            registrar_vehiculo("moto")
        elif opcion == '2':
            registrar_vehiculo("carro")
        elif opcion == '3':
            codigo = input("Ingrese el código del vehículo para cobrar: ")
            cobrar_salida(codigo)
        elif opcion == '4':
            mostrar_estadisticas()
        elif opcion == '5':
            print("Gracias por usar el sistema del parqueadero. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
