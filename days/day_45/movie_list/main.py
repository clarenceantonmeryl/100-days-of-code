import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2")
response.raise_for_status()
contents = response.text

soup = BeautifulSoup(contents, "html.parser")

print(soup.prettify())

# movies = soup.select_one(selector="h3.title")
# movies_div = soup.find(name='div', class_="listicle-item")

# movies = soup.select_one(selector=".listicle-item h3")

# print(movies)
