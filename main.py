# Top 100 Movies
import requests
import lxml
from bs4 import BeautifulSoup

# Get HTML document using requests
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
page_response = requests.get(url=URL)
page_html = page_response.text

# Use beautiful soup to parse the HTML
soup = BeautifulSoup(page_html, "lxml")

# Target CSS Selectors that has movie titles
movie_elements = soup.select(selector=".article-title-description .article-title-description__text .title")
top_100_movies = [movie.getText() for movie in movie_elements]
top_100_movies.reverse()

# Write movies list in text file
with open("100_movies_list.txt", "w", encoding="utf-8") as f:
    for movie in top_100_movies:
        f.write(movie + "\n")
