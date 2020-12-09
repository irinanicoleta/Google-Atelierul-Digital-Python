import requests
from bs4 import BeautifulSoup
import csv
from web_scrapper_handlers.extract_table_data import get_movie_from_table_row

URL = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

if __name__ == '__main__':
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, features='html.parser')

    table = soup.find('div', {'class': 'lister'}).find('table').find('tbody', {'class': 'lister-list'})

    table_rows = table.findAll('tr')

    cols = ['no', 'poster', 'title', 'year', 'IMDB rating', 'number of ratings']
    movies = list()
    for i in range(len(table_rows)):
        movies.append(get_movie_from_table_row(table_rows[i]))

    with open('info_movies.csv', 'w', newline='', encoding="utf-8") as file_csv:
        writer = csv.DictWriter(file_csv, fieldnames=cols)
        writer.writeheader()
        for i in range(len(movies)):
            writer.writerow(dict(zip(cols, movies[i])))
