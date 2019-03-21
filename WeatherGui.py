import requests
import json
import tkinter as tk
from tkinter import ttk


key = "ffb4f8b598bba4bdf868d38b6099cb46"
location = "Long Beach"

# ====================================
# API
# ====================================


class API:
    def __init__(self, api_key, location):
        self.api_key = api_key
        self.location = location

    # Method to retrieve data from API
    def get_weather(self):
        # Url api call for city
        url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}".format(self.location, self.api_key)
        r = requests.get(url)
        return r.json()


    def get_zip_code(self):
        print(zip)
        # zip_code = entry.get()
        # return zip_code

# ====================================
# GUI
# ====================================


class GUI:
    def __init__(self):
        window = tk.Tk()
        window.title("Weather App")
        window.geometry("225x320")

        # Creating Frame
        navigation_frame = ttk.LabelFrame(window, width=200, height=300, text="Type in your zip code")
        navigation_frame.pack()
        navigation_frame.config(height=100, width=200, padding=(30, 15))

        # Entry box
        zip_code = ttk.Entry(navigation_frame)
        zip_code.grid(pady=5)

        # Enter Button
        button = ttk.Button(navigation_frame, text="Find Weather", command=get_zip_code)
        button.grid()

        # Create new Frame for results
        results_frame = ttk.Frame(window, relief=tk.RIDGE)
        results_frame.pack()
        results_frame.config(height=200, width=200, padding=(30, 15))

        # Create text to display city
        searched_city = weather["name"] # this needs to extract only the city name
        city_label = ttk.Label(results_frame, text=searched_city)
        city_label.grid(row=0, column=0)

        # Create text to display status
        weather_status = weather["weather"][0]["description"]
        weather_status_label = ttk.Label(results_frame, text=weather_status)
        weather_status_label.grid(row=1, column=0)

        # Create temperature label
        temperature = str(weather["main"]["temp"]) + " F"
        temperature_label = ttk.Label(results_frame, text=temperature)
        temperature_label.grid()

        # Main Loop
        window.mainloop()

def main():
    api = API(key, location)
    weather = api.get_weather()
    print(weather)
#     weather = get_weather(key, "90803")
# print(weather)
# print(weather["name"])

if __name__ == '__main__':
    main()
