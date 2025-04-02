import requests
import argparse
from config import API_KEY

def get_weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "pl"
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            print(f"\nPogoda dla: {data['name']}, {data['sys']['country']}")
            print(f"Temperatura: {data['main']['temp']}°C")
            print(f"Opis: {data['weather'][0]['description']}")
            print(f"Wilgotność: {data['main']['humidity']}%")
        else:
            print("Błąd:", data.get("message", "Nieznany błąd"))

    except requests.exceptions.RequestException as e:
        print("Błąd połączenia:", e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sprawdź pogodę dla danego miasta.")
    parser.add_argument("city", help="Nazwa miasta (np. Warszawa)")

    args = parser.parse_args()
    get_weather(args.city)
