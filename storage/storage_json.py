import json
from storage.istorage import IStorage

class StorageJson(IStorage):
    def __init__(self, file_path):
        """
        Initializes the StorageJson object with the path to the JSON file.

        :param file_path: The path to the JSON file used for storage
        """
        self.file_path = file_path

    def list_movies(self):
        """
        Retrieves all the movies from the JSON file

        :return: A dictionary containing movie data, or an empty dict if file not found
        """
        try:
            with open(self.file_path, "r") as file:
                movies_data = json.load(file)
            return movies_data
        except FileNotFoundError:
            return {}


    def add_movie(self, title, year, rating, poster):
        """
        Adds a new movie to the JSON file.

        :param title: The title of the movie
        :param year: The release year of the movie
        :param rating: The rating of the movie
        :param poster: The URL or path to the movies poster
        :return: None
        """
        movies = self.list_movies()
        movies[title] = {"year": year, "rating": rating, "poster": poster}
        self._save_movies(movies)

    def delete_movie(self, title):
        """
        Deletes a movie from the JSON file.

        :param title: The title of the movie to delete.
        :return: None
        """
        movies = self.list_movies()
        if title in movies:
            del movies[title]
            self._save_movies(movies)


    def update_movie(self, title, rating):
        """
        Updates the rating of a movie in the JSON file.

        :param title: The title of the movie to update.
        :param rating: The new rating for the movie.
        :return: None
        """
        movies = self.list_movies()
        if title in movies:
            movies[title]["rating"] = rating
            self._save_movies(movies)

    def _save_movies(self, movies):
        """
        Saves the movie data to the JSON file.

        :param movies: The dictionary containing the movie data to save
        :return: None
        """
        with open(self.file_path, "w") as file:
            json.dump(movies, file, indent=4)
