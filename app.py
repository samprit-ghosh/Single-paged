from bs4 import BeautifulSoup
import requests

url = "https://dribbble.com/tags/front-end"
page = requests.get(url)
soup = BeautifulSoup(page.text,'html')
print(soup)


