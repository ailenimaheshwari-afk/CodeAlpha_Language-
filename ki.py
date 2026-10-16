
import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("span", class_="text")

print("Web Scraping Output:")
for i, quote in enumerate(quotes[:5], start=1):
    print(i, quote.text)
