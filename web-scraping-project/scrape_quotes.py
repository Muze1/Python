import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)
response.raise_for_status() # Abort for 4xx/5xx errors

