from storage_json import StorageJson
from movie_app import MovieApp
import title_menu as t


def main():
    storage = StorageJson('movies.json')  # Create the storage
    movie_app = MovieApp(storage)  # Create the MovieApp

    t.print_title()  # Print the title
    movie_app.run()  # Run the MovieApp

if __name__ == "__main__":
    main()
