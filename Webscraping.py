import requests
from bs4 import BeautifulSoup

# Specify the URL of the website to be scraped
url = "https://www.quora.com/"

# Send an HTTP request to the URL and receive the response
response = requests.get(url)

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the article titles and links on the homepage
articles = soup.find_all('article')
for article in articles:
    title = article.find('h2').text
    link = article.find('a')['href']
    print(title, link)