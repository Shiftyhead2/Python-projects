from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser
import requests


url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']


def get_weather(city):
    result = requests.get(url.format(city,api_key))
    if result:
        json = result.json()
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        temp_fahrenheight = (temp_kelvin - 273.15) * 9 / 5 + 35
        icon = json['weather'][0]['icon']
        weather = json['weather'][0]['main']
        description = json['weather'][0]['description']
        wind_speed = json['wind']['speed']
        wind_degree = json['wind']['deg']
        final = (city,country,temp_celsius,temp_fahrenheight,icon,weather,description,wind_speed,wind_degree)
        return final
    else:
        return None

def wind_deg_to_str2(deg):
    arr = ['NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW', 'N']
    return arr[int(abs((deg - 11.25) % 360) / 22.5)]



def search():
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        location_lbl['text'] = '{},{}'.format(weather[0],weather[1])
        temp_lbl['text'] = '{:.2f}°C,{:.2f}°F'.format(weather[2],weather[3])
        wind_direction = wind_deg_to_str2(weather[8])
        wind_lbl['text'] = 'Wind speed:{} m/s,Wind direction:{}'.format(weather[7],wind_direction)
        photo["file"] = "icons/{}.gif".format(weather[4])
        weather_lbl['text'] ='Weather:{}'.format(weather[5])
        desc_lbl['text'] = 'Description:{}'.format(weather[6])
    else:
        messagebox.showerror("Error","Cannot find city {}".format(city))

app = Tk()
app.title("Weather App")
app.geometry("700x400")
app.config(background = 'lightgrey')

text = Label(app,text = "Type in a city to see the current weather",background = 'lightgrey')
text.pack()
city_text = StringVar()
city_entry = Entry(app,textvariable = city_text)
city_entry.pack()

search_btn = Button(app,text = "search weather" ,width = 12, command = search)
search_btn.pack()


location_lbl = Label(app,text ="",font=("bold",20),background = 'lightgrey')
location_lbl.pack()


photo = PhotoImage(file = "")
image = Label(app,image = photo,background = 'lightgrey')
image.pack()

temp_lbl = Label(app,text = "",font=("bolt",15),background = 'lightgrey')
temp_lbl.pack()

wind_lbl = Label(app,text = "",font=("bolt",15),background = 'lightgrey')
wind_lbl.pack()

weather_lbl = Label(app,text = "",font =("bold",15),background = 'lightgrey')
weather_lbl.pack()

desc_lbl = Label(app,text = "",font =("bold",15),background = 'lightgrey')
desc_lbl.pack()

app.mainloop()