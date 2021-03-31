import requests
from datetime import datetime
import pywhatkit     #This is a module that can be used to send automatic WhatsApp messages


def get_weather_info():
    my_api = "{Replace your api here}"  
    location = "you{your city name}"  
    complete_api_link = "http://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+my_api

    api_link = requests.get(complete_api_link)
    api_data = api_link.json()

    if api_data['cod'] == '404':
        print(f"Invalid City: {location}, Please check your city name")
    else:
        city_temp = ((api_data['main']['temp']) - 273.15)
        weather_desc = api_data['weather'][0]['description']
        hmdt = api_data['main']['humidity']
        wind_spd = api_data['wind']['speed']
        date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    `   #The following lines were written for testing purpose
        #print(f"Weather stats for {location.upper()} || {date_time}")
        #print("Current temperature is: {}°C".format(city_temp))
        #print("current weather desc :", weather_desc)
        #print("Current humidity     :", hmdt, '%')
        #print("current wind speed   :", wind_spd, 'kmph')

        print("....................myabc360weather.....................")
        msg = f"""********** abc360 weather **********
Today's temperature in {location.upper()} is {city_temp}°C
Weather description: {weather_desc}
Don't forget to choose your clothing for today according to the weather conditions.
Have a nice day!"""
    return(msg)


if __name__ == '__main__':
    pywhatkit.sendwhatmsg('receivers_whatsApp_number', get_weather_info(), {hour}, {minute})
