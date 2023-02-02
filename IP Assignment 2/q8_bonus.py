import requests
import json

def weather():
    api_key = "1c4aaa597dd29ba9c44da6839c89fbf6"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = input("Enter city name : ")
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    print("City",x["name"])
    print("Weather",x["weather"][0])
    print("Temperature",x["main"])
    print("Wind",x["wind"])

def news():
    url = ('https://newsapi.org/v2/top-headlines?'
        'country=us&'
        'apiKey=a3219de17f424b1380562001868597fe')
    response1 = requests.get(url)
    response1 = response1.json()
    articles = response1['articles']
    x = 1
    for article in articles:
        print('------------------------------------------')
        print('\n'+"Title "+str(x))
        print(article['title'])
        print('\n'+"Description "+str(x))
        print(article['description'])
        print('\n'+"Published on "+str(x))
        print(article['publishedAt'])
        print('\n'+"Content "+str(x))
        print(article['content'])
        print('------------------------------------------')
        x+=1

weather1 = weather()
print()
news()