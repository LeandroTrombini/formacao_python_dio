from bs4 import BeautifulSoup

import requests

site = requests.get('https://g1.globo.com/').content

soup = BeautifulSoup(site, 'html.parser')

text = soup.find("span", class_="bstn-hl-title gui-color-primary gui-color-hover gui-color-primary-bg-after")

print(soup.prettify())
print(soup.title.string)