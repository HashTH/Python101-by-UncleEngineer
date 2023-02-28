import requests #pip install requests
from bs4 import BeautifulSoup #pip install beautifulsoup4
import csv

#real time millionaires
url = 'https://www.imdb.com/chart/top'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
movie_list = soup.find_all('td', class_='titleColumn')

data = []
for movie in movie_list:
    title = movie.find('a').text
    year = movie.find('span', class_='secondaryInfo').text.strip('()')
    rating = movie.find_next_sibling('td', class_='ratingColumn imdbRating').text.strip()
    data.append([title, year, rating])

with open('top_movies.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Title', 'Year', 'Rating'])
    writer.writerows(data)
