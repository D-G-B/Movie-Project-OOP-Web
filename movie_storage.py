import json
from movie import Movie


def load_movies():
    try:
        with open("movies.json", "r") as file:
            movies_data = json.load(file)
            return {
                title: Movie.from_dict(title, data)
                for title, data in movies_data.items()
            }
    except FileNotFoundError:
        return {}


def save_movies(movies):
    movies_dict = {
        title: movie.to_dict()
        for title, movie in movies.items()
    }
    with open("movies.json", "w") as file:
        json.dump(movies_dict, file, indent=4)


def add_movie(title, year, rating):
    movies = load_movies()
    movies[title] = Movie(title, year, rating)
    save_movies(movies)
    return True


def delete_movie(title):
    movies = load_movies()
    if title in movies:
        del movies[title]
        save_movies(movies)
        return True
    return False


def update_movie(title, rating):
    movies = load_movies()
    if title in movies:
        movies[title].rating = rating
        save_movies(movies)
        return True
    return False