from bs4 import BeautifulSoup
import requests
import csv

url = 'https://coinmarketcap.com/vi/faq/'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the sections that contain questions and answers
faq_sections = soup.find_all('section', class_='sc-d1a26d45-0')

# Open the existing CSV file for appending
with open('virtual_currency_faqs.csv', mode='a', encoding='utf-8', newline='') as csv_file:
    # Create a CSV writer object
    writer = csv.writer(csv_file)
    
    # Loop through each section and extract the question and answer
    for section in faq_sections:
        # Extract the question from the <h3> element
        question = section.find('h3').text.strip()
        
        # Extract the answer from the <p> elements
        answer_elements = section.find_all('p')
        # Join the text content of the <p> elements to form the answer
        answer = '\n'.join([element.text.strip() for element in answer_elements])
        
        # Write the question and answer to the CSV file
        writer.writerow([question, answer])