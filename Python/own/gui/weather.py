from tkinter import *
import requests
import json

root = Tk()
root.title('Weather App')
root.geometry('600x100')

def ziplookup():

    url = f'https://www.airnowapi.org/aq/observation/zipCode/historical/?format=application/json&zipCode={zipbutton.get()}&date=2021-09-10T00-0000&distance=25&API_KEY=4FFE94FC-FCC6-4349-985C-99FC923A436B'

    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0'
    }
    try:
        print('Trying to access API')
        api_request = requests.get(url, headers=headers)
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == 'Good':
            weather_color = '#0C0'
        elif category == 'Moderate':
            weather_color = '#FFFF00'
        elif category.endswith('Groups'):
            weather_color = '#ff9900'
        elif category == 'Unhealthy':
            weather_color ='#FF0000'
        elif category == 'Very Unhealthy':
            weather_color = '#990066'
        elif category == 'Hazardous':
            weather_color = '#660000'

        print('Success to access API')
        root.configure(bg=weather_color)
        myLabel = Label(root, text=f"{city} Air Quality: {quality} {category}",\
            font=('', 20), bg=weather_color).grid(row=1, column=0, columnspan=2)
    except Exception:
        api = 'Error...'


zipbutton = Entry(root)
zipbutton.grid(row=0, column=0, sticky=W+E+N+S)

zipButton = Button(root, text='Lookup Zipcode', command=ziplookup)
zipButton.grid(column=1, row=0, sticky=W+E+N+S)


root.mainloop()
