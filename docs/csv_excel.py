# csv filer
import requests
import pandas as pd



url = 'https://raw.githubusercontent.com/FBosler/Medium-Data-Extraction/master/sales_team.csv'
res = requests.get(url, allow_redirects=True)
with open('sales_team.csv','wb') as file:
    file.write(res.content)
sales_team = pd.read_csv('sales_team.csv')


# Excel filer
url = 'https://github.com/FBosler/Medium-Data-Extraction/blob/master/invoices.xlsx?raw=true'
res = requests.get(url, allow_redirects=True)
with open('invoices.xlsx','wb') as file:
    file.write(res.content)
invoices = pd.read_excel('invoices.xlsx')