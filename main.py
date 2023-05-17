import requests


def telegram_bot_send_text(bot_message):
    bot_token = 'YOUR_BOT_TOKEN'
    bot_chat_id = 'YOUR_CHAT_ID'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chat_id + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()


def get_weather_data():
    api_key = "YOUR_API_KEY"
    parameters = {
        "lat": 60.55,
        "lon": 15.28,
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


test = telegram_bot_send_text("It's going to rain in the next 12 hours. "
                              "You should probably take an umbrella if you go out.")
