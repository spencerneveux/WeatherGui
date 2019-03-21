import requests
import tkinter as tk
from tkinter import ttk

key = "ffb4f8b598bba4bdf868d38b6099cb46"

# ====================================
# GUI
# ====================================


class GUI:
    def __init__(self, master):
        master.title('Weather Forecast')
        master.geometry("200x250")
        master.resizable(False, False)
        master.configure(background='#000000')

        # Styling
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#000000')
        self.style.configure('nv.TLabel', background='#000000')
        self.style.configure('TButton', background='#000000')
        self.style.configure('TLabel', foreground='#000000', font=('Arial', 11), fg="#FFFFFF")

        self.window = ttk.Frame(master)
        self.window.pack()

        # Creating Frame
        self.navigation_frame = ttk.LabelFrame(self.window, width=200, height=300, text="Type in your zip code", style="nv.TLabel")
        self.navigation_frame.pack()
        self.navigation_frame.config(height=100, width=200, padding=(30, 15))

        # Entry box
        self.zip_code = ttk.Entry(self.navigation_frame)
        self.zip_code.grid(pady=5)

        # Enter Button
        self.button = ttk.Button(self.navigation_frame, text="Find Weather", command=self.update_results)
        self.button.grid()

        # Create new Frame for results
        self.results_frame = ttk.Frame(self.window, relief=tk.RIDGE, width=200, height=200)
        self.results_frame.pack(fill=None, expand=False)
        self.results_frame.config(height=200, width=200, padding=(30, 15))

        # Create text to display city
        searched_city = "City"
        self.city_label = ttk.Label(self.results_frame, text=searched_city)
        self.city_label.grid(row=0, column=0)

        # Create text to display status
        weather_status = "Weather"
        self.weather_status_label = ttk.Label(self.results_frame, text=weather_status)
        self.weather_status_label.grid(row=1, column=0)

        # Create temperature label
        # temperature =
        temperature = "N/A"
        self.temperature_label = ttk.Label(self.results_frame, text=temperature)
        self.temperature_label.grid()

    def get_zip_code(self):
        zip_code = self.zip_code.get()
        print(zip_code)
        return zip_code

        # Method to retrieve data from API
    def get_weather(self):
        zip_code = self.get_zip_code()
        # Url api call for city
        url = "https://api.openweathermap.org/data/2.5/weather?zip={}&units=imperial&appid={}".format(zip_code, key)
        r = requests.get(url)
        return r.json()

    def update_results(self):
        weather = self.get_weather()
        self.city_label.config(text=weather["name"])
        self.weather_status_label.config(text=weather["weather"][0]["description"])
        self.temperature_label.config(text=str(weather["main"]["temp"]) + " F")


def main():
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
