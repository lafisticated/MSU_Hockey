from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


headers = []
data = []

html = urlopen("http://www.collegehockeynews.com/stats/team/Minnesota/34/advanced,20152016")
soup = BeautifulSoup(html, "html.parser")

table = soup.findAll("table", {'class':'metrics sortable'})

print(table)

