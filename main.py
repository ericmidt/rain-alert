import requests
import os
from dotenv import load_dotenv

load_dotenv("C:/Python/EnvironmentVariables/.env")


def telegram_bot_send_text(bot_message):
    bot_token = os.environ.get("rain_alert_bot_token")
    bot_chat_id = os.environ.get("rain_alert_chat_id")
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chat_id + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()


def get_weather_data():
    api_key = os.environ.get("owm_api_key")
    parameters = {
        "lat": 48.41,
        "lon": 19.43,
        "appid": api_key,
        "exclude": "current,minutely,daily"
    }

    response = requests.get(url="https://api.openweathermap.org/data/2.8/onecall", params=parameters)
    print(response.status_code)
    weather_data = response.json()
    weather_hourly = []
    will_rain = False

    for hour in range(0, 11):
        weather_hourly.append(weather_data["hourly"][hour]["weather"][0]["id"])
        if int(weather_hourly[hour]) < 701:
            will_rain = True
    return will_rain


if get_weather_data():
    print(telegram_bot_send_text("It's going to rain in the next 12 hours. You should take an umbrella if you go out."))

