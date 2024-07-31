import pyttsx3
import datetime
from newsapi import NewsApiClient

# Initialize the TTS engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to get the current time of day
def get_time_of_day():
    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
        return "morning"
    elif 12 <= current_hour < 17:
        return "day"
    elif 17 <= current_hour < 21:
        return "evening"
    else:
        return "night"

# Function to fetch daily news
def get_daily_news(api_key):
    newsapi = NewsApiClient(api_key=api_key)
    top_headlines = newsapi.get_top_headlines(language='en', country='us')
    if top_headlines['status'] == 'ok':
        articles = top_headlines['articles']
        news_list = []
        for article in articles[:5]:  # Get top 5 news articles
            news_list.append(article['title'])
        return news_list
    else:
        return ["Sorry, I couldn't fetch the news at the moment."]

def main():
    # Get time of day
    time_of_day = get_time_of_day()
    
    # Greet the user based on the time of day
    greeting = f"Good {time_of_day} Binay ! Here are today's top news headlines:"
    speak(greeting)
    
    # Fetch and speak out daily news
    api_key = '84dad13096ab45cbb08fe1cbcbe1c487'  # Replace with your NewsAPI key
    daily_news = get_daily_news(api_key)
    for news in daily_news:
        speak(news)
    
if __name__ == "__main__":
    main()
