import csv
from istorage import IStorage

class StorageCsv(IStorage):
    """
    Implements the IStorage interface for storing movie data in a CSV file.
    """

    def __init__(self, file_path):
        """
        Initializes the StorageCsv object with the path to the CSV file.

        :param file_path: The path to the CSV file used for storage.
        """
        self.file_path = file_path

    def list_movies(self):
        """
        Retrieves all movies from the CSV file and returns them as a dictionary.

        :return: A dictionary containing movie data, or an empty dictionary if the file is not found or empty.
                 The keys are movie titles, and the values are dictionaries with 'year', 'rating', and 'poster'.
        """
        movies = {}
        try:
            with open(self.file_path, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    title = row['title']
                    try:
                        year = int(row['year'])
                        rating = float(row['rating'])
                    except ValueError:
                        print(f"Warning: Skipping movie '{title}' due to invalid year or rating format.")
                        continue
                    poster = row['poster']
                    movies[title] = {'year': year, 'rating': rating, 'poster': poster}
        except FileNotFoundError:
            pass  # Return empty dictionary if the file doesn't exist
        return movies

    def add_movie(self, title, year, rating, poster):
        """
        Adds a new movie to the CSV file.

        :param title: The title of the movie.
        :param year: The release year of the movie.
        :param rating: The rating of the movie.
        :param poster: The URL or path to the movie's poster.
        :return: None
        """
        movies = self.list_movies()
        movies[title] = {'year': year, 'rating': rating, 'poster': poster}
        self._save_movies(movies)

    def delete_movie(self, title):
        """
        Deletes a movie from the CSV file.

        :param title: The title of the movie to delete.
        :return: None
        """
        movies = self.list_movies()
        if title in movies:
            del movies[title]
            self._save_movies(movies)

    def update_movie(self, title, rating):
        """
        Updates the rating of a movie in the CSV file.

        :param title: The title of the movie to update.
        :param rating: The new rating for the movie.
        :return: None
        """
        movies = self.list_movies()
        if title in movies:
            movies[title]['rating'] = rating
            self._save_movies(movies)

    def _save_movies(self, movies):
        """
        Saves the movie data to the CSV file.

        :param movies: The dictionary containing movie data to save.
        :return: None
        """
        fieldnames = ['title', 'year', 'rating', 'poster']
        try:
            with open(self.file_path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for title, details in movies.items():
                    writer.writerow({'title': title, 'year': details['year'], 'rating': details['rating'], 'poster': details['poster']})
        except Exception as e:
            print(f"Error saving to CSV file: {e}")