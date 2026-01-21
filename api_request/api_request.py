import requests

api_key = "d97d08b9b934431cf0bac548cb9f794f"
api_url=f"https://api.weatherstack.com/current?access_key={api_key}&query=Sfax"
def get_weather_data():
    try :
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        raise
if __name__ == "__main__":
    weather_data = get_weather_data()
    print(weather_data)


def moch_fetch_data():
    
    return {'request': {'type': 'City', 'query': 'Sfax, Tunisia', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'Sfax', 'country': 'Tunisia', 'region': 'Sfax', 'lat': '34.741', 'lon': '10.760', 'timezone_id': 'Africa/Tunis', 'localtime': '2026-01-08 20:22', 'localtime_epoch': 1767903720, 'utc_offset': '1.0'}, 'current': {'observation_time': '07:22 PM', 'temperature': 11, 'weather_code': 113, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0008_clear_sky_night.png'], 'weather_descriptions': ['Clear '], 'astro': {'sunrise': '07:25 AM', 'sunset': '05:23 PM', 'moonrise': '11:00 PM', 'moonset': '10:40 AM', 'moon_phase': 'Waning Gibbous', 'moon_illumination': 75}, 'air_quality': {'co': '212.85', 'no2': '9.25', 'o3': '54', 'so2': '7.25', 'pm2_5': '11.25', 'pm10': '19.15', 'us-epa-index': '1', 'gb-defra-index': '1'}, 'wind_speed': 23, 'wind_degree': 256, 'wind_dir': 'WSW', 'pressure': 1028, 'precip': 0, 'humidity': 62, 'cloudcover': 25, 'feelslike': 9, 'uv_index': 0, 'visibility': 10, 'is_day': 'no'}}