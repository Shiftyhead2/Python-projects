from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser
import requests


url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']

bg = config['colors']['background']
letter_color = config['colors']['foreground']

def get_weather(city):
    result = requests.get(url.format(city,api_key))
    if result:
        json = result.json()
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_fells_kelvin = json['main']['feels_like']
        temp_celsius = round( temp_kelvin - 273.15)
        temp_fahrenheight =round((temp_kelvin * 9/5) - 459.67)
        temp_celsius_feels = round( temp_fells_kelvin - 273.15)
        temp_fahrenheight_feels = round((temp_fells_kelvin * 9/5) - 459.67)
        icon = json['weather'][0]['icon']
        weather = json['weather'][0]['main']
        description = json['weather'][0]['description']
        wind_speed = json['wind']['speed']
        wind_degree = json['wind']['deg']
        humidity = json['main']['humidity']
        final = (city,country,temp_celsius,temp_fahrenheight,icon,weather,description,wind_speed,wind_degree,humidity,temp_celsius_feels,temp_fahrenheight_feels)
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
        temp_lbl['text'] = 'Current: {}°C,{}°F,\nFeels like: {}°C,{}°F'.format(weather[2],weather[3],weather[10],weather[11])
        wind_direction = wind_deg_to_str2(weather[8])
        wind_lbl['text'] = 'Wind speed:{} m/s,\nWind direction:{}'.format(weather[7],wind_direction)
        humidity_lbl['text'] = 'Humidity:{}%'.format(weather[9])
        photo["file"] = "icons/{}.gif".format(weather[4])
        weather_lbl['text'] ='Weather:{},\n Description:{}'.format(weather[5],weather[6])

    else:
        messagebox.showerror("Error","Cannot find city {}".format(city))





app = Tk()
app.title("Weather App")
app.geometry("700x450")
app.config(background = bg)


text = Label(app,text = "Type in a city to see the current weather",background = bg,fg = letter_color)
text.pack()
city_text = StringVar()
city_entry = Entry(app,textvariable = city_text)
city_entry.pack()

search_btn = Button(app,text = "search weather" ,width = 12, command = search)
search_btn.pack()


location_lbl = Label(app,text ="",font=("bold",20),background = bg,fg = letter_color)
location_lbl.pack()


photo = PhotoImage(file = "")
image = Label(app,image = photo,background = bg)
image.pack()

temp_lbl = Label(app,text = "",font=("bolt",15),background = bg,fg = letter_color)
temp_lbl.pack()

wind_lbl = Label(app,text = "",font=("bolt",15),background = bg,fg = letter_color)
wind_lbl.pack()

humidity_lbl = Label(app,text = "",font=("bolt",15),background = bg,fg = letter_color)
humidity_lbl.pack()

weather_lbl = Label(app,text = "",font =("bold",15),background = bg,fg = letter_color)
weather_lbl.pack()


app.mainloop()