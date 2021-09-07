import requests
from bs4 import BeautifulSoup
import pandas as pd

preURL = 'https://en.wikipedia.org'
df = pd.DataFrame(columns = ['Region', 'Link', 'StadiumName'])
response = requests.get(
	url="https://en.wikipedia.org/wiki/List_of_stadiums_in_Europe",
)
soup = BeautifulSoup(response.content, 'html.parser')
links = soup.find_all("a", {"class": "mw-redirect"})

for item in links:
	url = preURL + item.get('href')
	stad_response = requests.get(url=url)
	stad_soup = BeautifulSoup(stad_response.content,'html.parser')
	tab_stad = stad_soup.find("table",attrs={'class':'infobox'})
	df = df.append({'Region':soup.title.string,'Link':url,'StadiumName':item.string},ignore_index = True)

	
