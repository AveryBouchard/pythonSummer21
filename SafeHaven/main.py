import requests
from bs4 import BeautifulSoup

r = requests.get('https://shsgateway.com/pinpoint-home/')

soup = BeautifulSoup(r.text, 'html.parser')

print(soup.prettify())
