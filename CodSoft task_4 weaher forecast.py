import tkinter as tk
import requests
import time
def getWeather(canvas):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=06c921750b9a82d8f5d1294e1586276f"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "MINIMUM TEMPERATURE: " + str(min_temp) + "°C" + "\n" + "MAXIMUM TEMPERATURE: " + str(
        max_temp) + "°C" + "\n" + "PRESSURE: " + str(pressure) + "\n" + "HUMIDITY: " + str(
        humidity) + "\n" + "WIND SPEED: " + str(wind) + "\n"
    label1.config(text=final_info)
    label2.config(text=final_data)
canvas = tk.Tk()
canvas.geometry("600x500")
canvas['bg']='cyan'
canvas.title("WEATHER FORECAST APPLICATION")
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")
textField = tk.Entry(canvas, justify='center', width=20, font=t, fg='red', bg='yellow')
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', getWeather)
label1 = tk.Label(canvas, font=t, fg='red', bg='cyan')
label1.pack()
label2 = tk.Label(canvas, font=f, fg='red', bg='cyan')
label2.pack()
canvas.mainloop()