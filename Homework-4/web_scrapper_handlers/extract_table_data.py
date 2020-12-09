def get_movie_from_table_row(html_row):
    info_movie = list()
    no = str(html_row.find('td', {'class': 'titleColumn'}))
    no = no[no.find('>')+1: no.find('<a')].strip()
    info_movie.append(no[:len(no)-1])
    poster = html_row.find('td', {'class': 'posterColumn'}).find('a')
    info_movie.append(poster.find('img'))
    title = str(html_row.find('td', {'class': 'titleColumn'}).find('a'))
    info_movie.append(title[title.find('>') + 1: title.find('</a>')])
    year = str(html_row.find('td', {'class': 'titleColumn'}).find('span'))
    info_movie.append(year[year.find('(')+1: year.find(')')])
    rating = str(html_row.find('td', {'class': 'ratingColumn imdbRating'}).find('strong'))
    info_movie.append(rating[rating.find('"')+1: rating.find('based')-1])
    info_movie.append(rating[rating.find('on ')+3: rating.find('user')-1])

    return info_movie

