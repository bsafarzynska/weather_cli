# 🌤️ Weather CLI App

A simple command-line weather application built with Python.  
It uses the OpenWeatherMap API to fetch and display current weather data for a given city.

---

## Features

- Get real-time weather information: temperature, description, humidity
- Simple CLI interface using `argparse`
- Error handling (invalid city name, connection issues)
- Language: Polish (can be easily adapted to English)

---

## How to Run

1. Clone this repository and navigate into the project folder:
```bash
git clone https://github.com/bsafarzynska/weather_cli.git
cd weather_cli
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `config.py` file with your own API key:
```python
# config.py
API_KEY = "YOUR_API_KEY_HERE"
```

Alternatively, copy the provided `example_config.py`:
```bash
cp example_config.py config.py
```

4. Run the app with a city name:
```bash
python main.py Warsaw
```

---

## Example Output

```
Weather for: Warsaw, PL
Temperature: 13.7°C
Description: clear sky
Humidity: 52%
```

---

## Built With

- Python 3
- requests
- argparse
- OpenWeatherMap API
