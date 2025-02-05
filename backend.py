import requests

API_KEY = "d522e70e36a474ed58047847e1f917b1"

def get_data(place=None, forecast_days=1, kind="Temperature"):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    nr_values = 8 * forecast_days
    times = [data['list'][i]['dt_txt'] for i in range(nr_values)]
    if kind == "Temperature":
        filtered_data = [data['list'][i]['main']['temp'] for i in range(nr_values)]
    if kind == "Sky":
        filtered_data = [data['list'][i]['weather'][0]['main'] for i in range(nr_values)]
    return filtered_data, times

if __name__ == "__main__":
    print(get_data(place='lahore', forecast_days=3, kind="Sky"))