tasas_de_cambio = {'dolar': 1.0,'euro': 0.85,'libra esterlina': 0.73,'dolar canadiense': 1.25,'dolar australiano': 1.30,'real': 5.30,'peso mexicano': 20.00,'nuevo sol': 3.80}
def realizar_cambio():
    print("Opciones de moneda:")
    for moneda in tasas_de_cambio.items():
        print(f"{moneda}")
    moneda_A = input("Ingrese la moneda a cambiar: ")
    moneda_B = input("Ingrese la moneda de destino: ")
    if moneda_A not in tasas_de_cambio or moneda_B not in tasas_de_cambio:
        print("Moneda no válida. Por favor, ingrese una moneda válida.")
        return
    cantidad = float(input(f"Ingrese la cantidad de {moneda_A}: "))
    tasa_A = tasas_de_cambio[moneda_A]
    tasa_B = tasas_de_cambio[moneda_B]
    producto=cantidad*(tasa_B/tasa_A)
    print(f"{cantidad} {moneda_A} equivale a {producto} {moneda_B}")
def mostrar_tasas_de_cambio():
    print("Tasas de cambio disponibles:")
    for moneda, tasa in tasas_de_cambio.items():
        print(f"{moneda}: {tasa}")

    