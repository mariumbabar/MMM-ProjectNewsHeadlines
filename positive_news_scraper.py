import requests
from bs4 import BeautifulSoup

def get_headlines():
    # Fetch headlines from the Positive News website
    url = "https://www.positive.news/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    headlines = soup.find_all("h2", class_="entry-title")
    return [headline.text.strip() for headline in headlines]
