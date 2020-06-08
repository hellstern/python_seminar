# Import af CSV og Excel til DataFrame
# Filer placert lokat
import pandas as pd

# CSV
seals_team = pd.read_csv("sales_team.csv")
print(seals_team)

# Excel
invoices = pd.read_excel("invoices.xlsx")
print(invoices)



# Hent fra URL - CSV og Excel
# Filer er placert på GitHub
import requests

# CSV
url = "https://hellstern.github.io/python_seminar/sales_team.csv"
res = requests.get(url, allow_redirects=True)
with open('sales_team.csv', 'wb') as file:
    file.write(res.content)
sales_team = pd.read_csv('sales_team.csv')

print(sales_team)

# Excel
url = "https://hellstern.github.io/python_seminar/invoices.xlsx"
res = requests.get(url, allow_redirects=True)
with open('invoices.xlsx', 'wb') as file:
    file.write(res.content)
invoices = pd.read_excel('invoices.xlsx')

print(invoices)
