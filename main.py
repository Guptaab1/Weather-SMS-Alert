import requests
from twilio.rest import client

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "14593306f234912cf3d301asadfsad455"
account_sid = "14593306f234912cf3d301dfsdfdsafds"
auth_token = "14593306f234912cf3d301adbsfdsfsdf"

weather_params = {
    "lat": 28.550925,
    "lon": 77.348681,
    "appid": api_key,
    "exclude": "current, minutely, daily"
}

response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = client(account_sid, auth_token)
    message = client.messages \
        .create(
        body= "It's going to rain today. Remember to bring an umbrella.",
        from="+15022553356",
        to="+15022553356",
    )
    print(message.status)