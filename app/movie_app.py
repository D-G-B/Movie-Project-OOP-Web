from storage.istorage import IStorage
from app import title_menu as tm
from app.title_menu import title_text
from dotenv import  load_dotenv
import random
import statistics
import requests
import os


load_dotenv()

class MovieApp:
    """
    A class that manages the movie application.
    It handles the menu, commands and interacts with the storage
    """

    def __init__(self, storage: IStorage):
        """
        Initializes the MovieApp  with a storage object.

        :param storage: An object that implements the IStorage interface.
        :return: None
        """
        self._storage = storage
        self._api_key = os.environ.get('OMDB_API_KEY')
        if not self._api_key:
            print("Warning: OMDb API key not found in environment variables. 'Add Movie' will be limited.")


    def _list_all_movies(self):
        """
        Lists all the movies in the storage.

        :return: None
        """
        movies = self._storage.list_movies()
        if movies:
            print("List of Movies:")
            for title, details in movies.items():
                print(f"- {title}: Year={details['year']}, Rating={details['rating']}, Poster={details['poster']}")
        else:
            print("No movies in the storage.")


    def _add_new_movie(self):
        """
        Adds a new movie to the storage by fetching details from OMDb API.

        :return: None
        """
        if not self._api_key:
            print("OMDb API key is required for this feature. Please set the OMDB_API_KEY environment variable.")
            return

        title = input("Enter the title of the movie to add: ")
        api_url = f"http://www.omdbapi.com/?t={title}&apikey={self._api_key}&r=json"

        try:
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()

            if data.get('Response') == 'True':
                movie_title = data.get('Title')
                year = data.get('Year')
                rating = data.get('imdbRating')
                poster = data.get('Poster')

                if movie_title and year and rating and poster and rating != 'N/A':
                    self._storage.add_movie(movie_title, year, rating, poster)
                    print(f"Movie '{movie_title}' added successfully.")
                else:
                    print(f"Could not retrieve complete information for '{title}' from OMDb.")
            else:
                error = data.get('Error')
                print(f"Error fetching movie '{title}' from OMDb: {error}")

        except requests.exceptions.RequestException as e:
            print(f"Error connecting to OMDb API: {e}")
        except ValueError:
            print("Error decoding JSON response from OMDb API.")


    def _delete_existing_movie(self):
        """
        Deletes a movie from the storage.

        :return: None
        """
        title = input("Enter the title of the movie to delete: ")
        if title in self._storage.list_movies():
            self._storage.delete_movie(title)
            print(f"Movie '{title}' deleted successfully.")
        else:
            print(f"Movie '{title}' not found.")


    def _update_existing_movie(self):
        """
        Updates an existing movie's rating in the storage.

        :return: None
        """
        title = input("Enter the title of the movie to update: ")
        if title in self._storage.list_movies():
            try:
                rating = float(input("Enter the new rating (0-10): "))
                if not 0 <= rating <= 10:
                    raise ValueError
                self._storage.update_movie(title, rating)
                print(f"Rating for '{title}' updated to {rating}.")
            except ValueError:
                print("Invalid rating. Please enter a number between 0 and 10.")
        else:
            print(f"Movie '{title}' not found.")


    def _show_stats(self):
        """
        Displays statistics about the movies in the storage.

        :return: None
        """
        movies = self._storage.list_movies()
        if movies:
            ratings = [float(details['rating']) for details in movies.values() if details['rating'] != 'N/A' and self._is_float(details['rating'])]
            if ratings:
                print(f"Average rating: {statistics.mean(ratings):.2f}")
                print(f"Median rating: {statistics.median(ratings):.2f}")
                print(f"Best rating: {max(ratings)}")
                print(f"Worst rating: {min(ratings)}")
            else:
                print("No valid ratings available to calculate statistics.")
        else:
            print("No movies in the storage to calculate statistics.")

    @staticmethod
    def _is_float(value):
        try:
            float(value)
            return True
        except ValueError:
            return False


    def _show_random_movie(self):
        """
        Displays a random movie from the storage.

        :return: None
        """
        movies = self._storage.list_movies()
        if movies:
            random_movie = random.choice(list(movies.keys()))
            details = movies[random_movie]
            print(f"Random movie: {random_movie} (Year: {details['year']}, Rating: {details['rating']}, Poster: {details['poster']})")
        else:
            print("No movies in the storage to pick a random one.")


    def _search_movies(self):
        """
        Searches for movies in the storage by title.

        :return: None
        """
        search_term = input("Enter the title (or part of it) to search for: ").lower()
        found_movies = {}
        movies = self._storage.list_movies()
        for title, details in movies.items():
            if search_term in title.lower():
                found_movies[title] = details
        if found_movies:
            print("Search Results:")
            for title, details in found_movies.items():
                print(f"- {title}: Year={details['year']}, Rating={details['rating']}, Poster={details['poster']}")
        else:
            print(f"No movies found matching '{search_term}'.")


    def _show_movies_by_rating(self):
        """
        Displays movies sorted by rating (highest to lowest).

        :return: None
        """
        movies = self._storage.list_movies()
        if movies:
            # Filter out movies with 'N/A' or invalid ratings before sorting
            valid_movies = {title: details for title, details in movies.items() if details['rating'] != 'N/A' and self._is_float(details['rating'])}
            sorted_movies = sorted(valid_movies.items(), key=lambda item: float(item[1]['rating']), reverse=True)
            if sorted_movies:
                print("Movies sorted by rating (highest to lowest):")
                for title, details in sorted_movies:
                    print(f"- {title}: Rating={details['rating']}, Year={details['year']}, Poster={details['poster']}")
            else:
                print("No movies with valid ratings to sort.")
        else:
            print("No movies in the storage.")


    def _show_movies_by_year(self):
        """
        Displays movies sorted by year (oldest to newest).

        :return: None
        """
        movies = self._storage.list_movies()
        if movies:
            # Attempt to convert year to integer for sorting, handle errors
            def sort_key(item):
                try:
                    return int(item[1]['year'])
                except ValueError:
                    return float('inf')  # Put movies with invalid years at the end by making them infinitely big

            sorted_movies = sorted(movies.items(), key=sort_key)
            print("Movies sorted by year (oldest to newest):")
            for title, details in sorted_movies:
                print(f"- {title}: Year={details['year']}, Rating={details['rating']}, Poster={details['poster']}")
        else:
            print("No movies in the storage.")


    @staticmethod
    def _exit():
        """
        Exits the application.

        :return: bool: False to stop the application loop.
        """
        return False

    def _generate_website(self):
        """
        Generates the movie website based on the stored movies and the template.

        :return: None
        """
        movies = self._storage.list_movies()

        script_dir = os.path.dirname(os.path.abspath(__file__))
        template_path = os.path.join(script_dir, '..', 'web', '_static', 'index_template.html')
        output_path = os.path.join(script_dir, '..', 'web', '_static', 'index.html')

        app_title_lines = title_text.strip("\n").split("\n")
        red = "#ff4d4d"
        yellow = "#ffff66"
        orange = "#ffa500"

        colored_title_html = ""
        for line in app_title_lines:
            colored_line = ""
            for char in line:
                color = random.choice([red, yellow, orange])
                colored_line += f'<span style="color:{color};">{char}</span>'
            colored_title_html += f'<p class="ascii-title-line">{colored_line}</p>'  # Added a class

        try:
            with open(template_path, 'r', encoding='utf-8') as template_file:
                template_content = template_file.read()
        except FileNotFoundError:
            print(f"Error: Template file not found at {template_path}")
            return

        movie_grid_html = ""
        for title, details in movies.items():
            movie_grid_html += f"""
            <div class="movie-item">
                <img src="{details['poster']}" alt="{title} Poster">
                <div class="movie-item-details">
                    <h3>{title}</h3>
                    <p>Year: {details['year']}</p>
                    <p>Rating: {details['rating']}</p>
                </div>
            </div>
            """

        website_content = template_content.replace("__TEMPLATE_MOVIE_GRID__", movie_grid_html)
        website_content = website_content.replace("<h1>__TEMPLATE_TITLE__</h1>", colored_title_html)

        try:
            with open(output_path, 'w', encoding='utf-8') as output_file:
                output_file.write(website_content)
            print("Website was generated successfully.")
        except Exception as e:
            print(f"Error generating website: {e}")


    def run(self):
        """
        Runs the movie application.
        This method displays the menu, gets user input,
        and executes the corresponding command.

        :return: None
        """
        running = True
        while running:
            tm.print_menu()
            choice = input("Enter choice: ")
            if choice == "0":
                running = MovieApp._exit()
            elif choice == "1":
                self._list_all_movies()
            elif choice == "2":
                self._add_new_movie()
            elif choice == "3":
                self._delete_existing_movie()
            elif choice == "4":
                self._update_existing_movie()
            elif choice == "5":
                self._show_stats()
            elif choice == "6":
                self._show_random_movie()
            elif choice == "7":
                self._search_movies()
            elif choice == "8":
                self._show_movies_by_rating()
            elif choice == "9":
                self._show_movies_by_year()
            elif choice == "10":
                self._generate_website()
            else:
                print("Invalid choice, please try again.")
        print("Goodbye!")