from storage_json import StorageJson
from storage_csv import StorageCsv
from movie_app import MovieApp
import title_menu as t

def main():
    # Test with JSON storage
    print("--- Testing with JSON Storage ---")
    json_storage = StorageJson('movies.json')
    json_app = MovieApp(json_storage)
    t.print_title()
    json_app.run()

    # Test with CSV storage
    print("\n--- Testing with CSV Storage ---")
    csv_storage = StorageCsv('movies.csv')
    csv_app = MovieApp(csv_storage)
    t.print_title()
    csv_app.run()

if __name__ == "__main__":
    main()