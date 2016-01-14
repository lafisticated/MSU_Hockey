from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


headers = []
data = []

html = urlopen("http://www.collegehockeynews.com/stats/")
soup = BeautifulSoup(html, "html.parser")

table = soup.find("table", {'class':'data sortable'})

table_head = table.find('thead')
rows = table_head.find_all('tr')
for row in rows:
    cols = row.find_all('th')
    cols = [ele.text.strip() for ele in cols]
    headers.append([ele for ele in cols if ele])

headers.pop(0)
real_header = headers.pop(0)

table_body = table.find('tbody')
rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])

my_df = pd.DataFrame(data)
csv_name = "standardstats.csv"
my_df.to_csv(csv_name, index=False, header=real_header)

