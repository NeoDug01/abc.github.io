from bs4 import BeautifulSoup
import requests
import csv

url = 'https://www.irs.gov/vi/individuals/international-taxpayers/frequently-asked-questions-on-virtual-currency-transactions'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

divs = soup.find_all('div', {'class': 'collapsible-item-heading panel-heading'})

with open('virtual_currency_faqs.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Question', 'Answer'])

    for div in divs:
        heading = div.find('h4')
        paragraph = div.find_next_sibling('div').find('p')
        writer.writerow([heading.text.strip(), paragraph.text.strip()])