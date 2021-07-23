"""
В файле хранятся данные с сайта IMDB.
Скопированные данные хранятся в файле ./data_hw5/ ratings.list.
Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла  top250_movies.txt – названия файлов,
ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.

"""
import json

try:
    with open('ratings_list.txt') as rating_list:
        top250_films = []
        for num, line in enumerate(rating_list):
            if 28 <= num <= 277:
                top250_films.append(line.split()[2:])

        top_films = []
        for name in top250_films:
            name = name[1:-1]
            top_films.append(name)
        with open('top250_movies.txt', 'w') as top250:
            for name in top_films:
                top250.write(' '.join(name) + '\n')

        rating_films = {}
        for rating in top250_films:
            count = 0
            for rating_temp in top250_films:
                if rating[0] in rating_temp:
                    count += 1
                    rating_films[rating[0]] = count
        with open('ratings.txt', 'w') as ratings_top250:
            json.dump(rating_films, ratings_top250, indent='\n')

        year_films = {}
        for year in top250_films:
            count = 0
            for year_film in top250_films:
                if year[-1] in year_film:
                    count += 1
            year_films[year[-1].strip('()')] = count
        with open('year_films.txt', 'w') as year:
            json.dump(year_films, year, indent='\n')
except FileExistsError:
    print("Файл не существует")

