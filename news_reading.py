import requests
import json
from win32com.client import Dispatch


def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.speak(str)

if __name__ == "__main__":
    speak("News for today...Lets begin")
    url = "https://newsapi.org/v2/everything?q=tesla&from=2021-07-04&sortBy=publishedAt&apiKey=000724a8ba4043018bd4ea0e48cf7d5e"
    news = requests.get(url).text
    news_dict = json.loads(news)
    print(news_dict['status'])
    arts = news_dict['articles']
    for article in arts:
        speak(article['title'])
        print(article['title'])
        speak("Moving to the next news...Listen carefully")

    speak("Thanks for listening")
