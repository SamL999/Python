from bs4 import BeautifulSoup
import requests
import re

resp = requests.get("https://bit.ly/3gkZaJa")

soup = BeautifulSoup(resp.text, "lxml")                   

titles = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])

for title in titles :
    print (title.text.strip())

