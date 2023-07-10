import requests
from bs4 import BeautifulSoup

url = "https://fr.quora.com/search?q=crypto"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

questions = soup.find_all('a', {'class': 'question_link'})
answers = soup.find_all('div', {'class': 'ui_qtext_expanded'})

for i in range(len(questions)):
    question = questions[i].text.strip()
    answer = answers[i].text.strip()
    print("Question {}: {}".format(i+1, question))
    print("Answer {}: {}".format(i+1, answer))