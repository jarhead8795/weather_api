import requests


WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
COORD_URL = "http://api.openweathermap.org/geo/1.0/zip"
HEADERS_JSON  = {"Accept": "application/json","Content-Type": "application/json"}
  
  
def get_location(zip_code: str, country_code: str = None, api_key=None) -> list:
    """
    Get the location coordinates from the given zip code and country code
    
    Args:
        zip_code (str) : Zip code
        country_code (str): Country Code (Optional)
        api_key (str): A valid API key for the weather api.
    Returns:
        Location data (dict)
    """
    url = f"{COORD_URL}?zip={zip_code}&appid={api_key}"
    
    if country_code:
        url = url + "&country_code={country_code}"

    response = requests.get(url, headers = HEADERS_JSON)
    response.raise_for_status()

    return response.json()


def get_weather_forecast(lat:str = None, lon: str = None, units: str = 'imperial', api_key=None) -> dict:
    """
    Gets the weather forecast for the given coordinates
    
    Args:
        lat (str) : latitude coordinates
        lon (str):  longitude coordinates
        units(str): Display type. Default is 'imperial' (Optional)
        api_key (str): A valid API key for the weather api.
    Returns:
        Weather data (dict)
    """
    url = f"{WEATHER_URL}?lat={lat}&lon={lon}&units={units}&appid={api_key}"

    response = requests.get(url, headers = HEADERS_JSON)
    response.raise_for_status()

    return response.json()
