import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "your_API_key"           # api_key = os.environ.get("OWM_API_KEY")
MY_LAT = 13.079938
MY_LONG = 80.272210
account_sid = "your_acc_sid"
auth_token = "your_acc_tkn"        # auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4
}
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Rain expected in the next 12 hours—grab your umbrella! ☔️ Stay dry!",
        from_="+1234567890",
        to="+098765431",
    )

    print(message.status)
