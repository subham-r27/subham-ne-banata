import requests
from bs4 import BeautifulSoup
import openpyxl

# Step 1: Load the local HTML file
url = "http://127.0.0.1:5500/index.html"
response = requests.get(url)

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Find the table and extract data
table = soup.find('table', id='data-table')

# Prepare data to be written to Excel
data = []
header_row = table.find('thead').find_all('th')
data.append([header.text.strip() for header in header_row])

# Extract data from table body
for row in table.find('tbody').find_all('tr'):
    columns = row.find_all('td')
    data.append([col.text.strip() for col in columns])

# Step 4: Write data to Excel
wb = openpyxl.Workbook()
ws = wb.active

for row in data:
    ws.append(row)

wb.save("output.xlsx")

print("Data has been written to output.xlsx")
