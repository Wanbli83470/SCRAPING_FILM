from requests import get as g
from bs4 import BeautifulSoup as bs
import pandas as pd

requête = g("https://www.imdb.com/search/title?release_date=2017-01-01,2017-12-31&sort=num_votes,desc&ref_")

html_soup = bs(requête.text, "html.parser")

movie_container = html_soup.find_all('div', class_="lister-item mode-advanced")
print(len(movie_container))

#titre d'un film
first_movie = movie_container[0]
first_name = first_movie.h3.a.text
print(first_name)

# Année de sortie
first_years = first_movie.h3.find("span", class_="lister-item-year text-muted unbold").text
print(first_years)

# Note
first_imdb = float(first_movie.strong.text)
print(first_imdb)

# Note metascore
first_metascore = first_movie.find("span", class_="metascore favorable")
first_metascore = int(first_metascore.text)
print(first_metascore)

# Nombres de votes
first_votes = first_movie.find("span", attrs = {'name': 'nv'})
first_votes = first_votes['data-value']
first_votes = int(first_votes)
print(first_votes)

# On crée des listes pour récupérer toutes les informations :
names = []
years = []
imdb_ratings = []
metascores = []
votes = []

for container in movie_container :
    if container.find('div', class_="ratings-metascore") is not None:
        # titre du film
        name = container.h3.a.text
        names.append(name)
        # année de sortie
        year = container.h3.find("span", class_="lister-item-year text-muted unbold").text
        years.append(year)
        # note imdb_ratings
        imdb_rating = float(container.strong.text)
        imdb_ratings.append(imdb_rating)
        # metascores
        metascore = container.find("span", class_="metascore favorable")
        metascores.append(metascore)
        # nb de votes
        vote = container.find("span", attrs={'name': 'nv'})
        vote = vote['data-value']
        vote = int(vote)

        votes.append(vote)

print(len(names))

test_dataframe = pd.DataFrame({
    'movie': names,
    'year': years,
    'imdb': imdb_ratings,
    'metascore': metascores,
    'vote' : votes,
})
print(test_dataframe)