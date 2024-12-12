import requests
import schedule
import time

# Your API keys
API_KEY_1 = 'df7bf0a71e03401182650cf58331ebfc'
API_KEY_2 = 'fd1a10c7edmsh5675d4066edd546p110163jsn5a2a4059da46'

# Base URLs of your APIs (replace with actual URLs)
API_URL_1 = 'https://newsapi.org/v2/everything?q=keyword&apiKey=API_KEY'
API_URL_2 = 'hhttps://google-news13.p.rapidapi.com'

def fetch_news_from_api_1():
    """Fetches news from API 1."""
    try:
        response = requests.get(f"{API_URL_1}{API_KEY_1}")
        response.raise_for_status()
        news_data = response.json()  # Assuming the API returns JSON
        print("Fetched news from API 1:", news_data)
        # Process and save the news data as needed
    except requests.RequestException as e:
        print(f"Error fetching news from API 1: {e}")

def fetch_news_from_api_2():
    """Fetches news from API 2."""
    try:
        response = requests.get(f"{API_URL_2}{API_KEY_2}")
        response.raise_for_status()
        news_data = response.json()  # Assuming the API returns JSON
        print("Fetched news from API 2:", news_data)
        # Process and save the news data as needed
    except requests.RequestException as e:
        print(f"Error fetching news from API 2: {e}")

def fetch_news():
    """Fetches news from both APIs."""
    print("Fetching news...")
    fetch_news_from_api_1()
    fetch_news_from_api_2()
    print("News fetching completed.")

# Schedule the task every 5 minutes
schedule.every(5).minutes.do(fetch_news)

# Fetch news once before the scheduler starts
fetch_news()

print("Scheduler started. Fetching news every 5 minutes...")

# Keep the scheduler running
while True:
    schedule.run_pending()
    time.sleep(1)
