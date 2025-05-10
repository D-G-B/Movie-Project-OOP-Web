from app.movie_app import MovieApp
from app.title_menu import print_title
from storage.storage_json import StorageJson


def main():
    # with JSON storage
    print("--- Running with JSON Storage ---")
    json_storage = StorageJson('data/movies.json')
    json_app = MovieApp(json_storage)
    print_title()
    json_app.run()

    # with CSV storage
    # print("\n--- Running with CSV Storage ---")
    # csv_storage = StorageCsv('movies.csv')
    # csv_app = MovieApp(csv_storage)
    # print_title()
    # csv_app.run()

if __name__ == "__main__":
    main()