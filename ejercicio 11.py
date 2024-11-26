def calcular_promedios():
    N = int(input("Ingrese el número de asignaturas: "))

    total_notas = 0
    total_creditos = 0

    for i in range(N):
        print(f"\nAsignatura {i+1}:")
        nota = float(input("Ingrese la nota: "))
        creditos = int(input("Ingrese la cantidad de créditos: "))

        total_notas += nota
        total_creditos += nota * creditos

    media_aritmetica = total_notas / N
    total_creditos_sumados = sum([int(input(f"Ingrese los créditos para la asignatura {i+1}: ")) for i in range(N)])
    media_ponderada = total_creditos / total_creditos_sumados

    print("\nResultados:")
    print(f"Media Aritmética: {media_aritmetica:.2f}")
    print(f"Media Aritmética Ponderada: {media_ponderada:.2f}")

calcular_promedios()

