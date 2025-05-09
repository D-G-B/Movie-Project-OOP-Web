from istorage import IStorage
import title_menu as tm
import random
import statistics

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
        Adds a new movie to the storage.

        :return: None
        """
        title = input("Enter movie title: ")
        year = input("Enter release year: ")
        try:
            rating = float(input("Enter rating (0-10): "))
            if not 0 <= rating <= 10:
                raise ValueError
        except ValueError:
            print("Invalid rating. Please enter a number between 0 and 10.")
            return
        poster = input("Enter poster URL: ")
        self._storage.add_movie(title, year, rating, poster)
        print(f"Movie '{title}' added successfully.")

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
            ratings = [details['rating'] for details in movies.values()]
            print(f"Average rating: {statistics.mean(ratings):.2f}")
            print(f"Median rating: {statistics.median(ratings)}")
            print(f"Best rating: {max(ratings)}")
            print(f"Worst rating: {min(ratings)}")
        else:
            print("No movies in the storage to calculate statistics.")

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
            sorted_movies = sorted(movies.items(), key=lambda item: item[1]['rating'], reverse=True)
            print("Movies sorted by rating (highest to lowest):")
            for title, details in sorted_movies:
                print(f"- {title}: Rating={details['rating']}, Year={details['year']}, Poster={details['poster']}")
        else:
            print("No movies in the storage.")

    def _show_movies_by_year(self):
        """
        Displays movies sorted by year (oldest to newest).

        :return: None
        """
        movies = self._storage.list_movies()
        if movies:
            sorted_movies = sorted(movies.items(), key=lambda item: item[1]['year'])
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
                running = self._exit()
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
            else:
                print("Invalid choice, please try again.")
        print("Goodbye!")