#Implement a basic web scraping program using a library like BeautifulSoup.
print ("\nSubi - Day 44 of #100DaysOfCode\n") 
print("\nImplement a basic web scraping program using a library like BeautifulSoup\n")

import requests
from bs4 import BeautifulSoup

url = 'https://example.com'

response = requests.get(url)

if response.status_code == 200:
    
    soup = BeautifulSoup(response.text, 'html.parser')

    article_titles = soup.find_all('h2')  

    for title in article_titles:
        print(title.text)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
