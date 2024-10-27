import os, requests

# Set up api key
api_key = os.getenv("OPEN_WEATHER_MAP_KEY") 


def get_data(place, forecast_days=None, kind=None):
    url = "https://api.openweathermap.org/data/2.5/forecast?" \
        f"q={place}&" \
        f"appid={api_key}"
    
    response = requests.get(url)
    data = response.json()

    filtered_data = data["list"]
    filtered_data = filtered_data[:8*forecast_days]
        
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3, kind="Sky"))