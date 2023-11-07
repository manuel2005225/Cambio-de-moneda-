import requests
import json
import matplotlib.pyplot as plt

# API de cambio de moneda
url = "https://api.currencyfreaks.com/v2.0/rates/latest?apikey=e2277eb0e898401e839242d24c90833d&symbols=EUR,GBP,COP,ARS,MXN,PKR,INR,CAD,AUD,AED,ILS,RUB,CHF,JPY,CNY,BRL&base=USD"

# Monedas disponibles
MONEY_CODES = {
    "COP":"Peso colombiano",
    "ARS":"Peso argentino",
    "MXN":"Peso mexicano",
    "PKR":"Rupia pakistaní",
    "INR":"Rupia india",
    "AED":"Dírham de los Emiratos Árabes Unidos",
    "ILS":"Nuevo séquel",
    "RUB":"Rublo ruso",
    "EUR": "Euro",
    "USD": "Dólar estadounidense",
    "GBP": "Libra esterlina",
    "JPY": "Yen japonés",
    "CHF": "Franco suizo",
    "CAD": "Dólar canadiense",
    "AUD": "Dólar australiano",
    "CNY": "Yuan chino",
    "BRL": "Real brasileño",
}

def get_exchange_rates():
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.content)
    else:
        return None

# Función para convertir una cantidad de una moneda a otra
def convert_currency(amount, from_currency, to_currency):
    exchange_rates = get_exchange_rates()
    if exchange_rates is None:
        return None

    from_rate = exchange_rates["rates"][from_currency]
    to_rate = exchange_rates["rates"][to_currency]

    return amount * (to_rate / from_rate)

# Página web
def main():
    # Crear un formulario para obtener la cantidad y las monedas
    amount = input("Cantidad a convertir: ")
    from_currency = input("Moneda de origen: ")
    to_currency = input("Moneda de destino: ")

    # Obtener las tasas de cambio
    exchange_rates = get_exchange_rates()
    if exchange_rates is None:
        print("Error al obtener las tasas de cambio.")
        return

    # Convertir la cantidad
    converted_amount = convert_currency(float(amount), from_currency, to_currency)

    # Mostrar el resultado
    print(f"{amount} {MONEY_CODES[from_currency]} = {converted_amount} {MONEY_CODES[to_currency]}")

    # Obtener los datos de las tasas de cambio
    rates = exchange_rates["rates"]

    # Crear la gráfica
    plt.plot(rates.keys(), rates.values())
    plt.xlabel("Moneda")
    plt.ylabel("Tasa de cambio")

    # Mostrar la gráfica
    plt.show()

if __name__ == "__main__":
    main()