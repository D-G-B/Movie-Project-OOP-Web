import random
from statistics import median
import movie_storage as storage


def get_valid_year():
    """Get a valid year input from the user"""
    while True:
        try:
            year = int(input("Enter movie year: "))
            if 1888 <= year <= 2025:  # First movie was in 1888, allow for upcoming movies
                return year
            print("Please enter a year between 1888 and 2025. :( ")
        except ValueError:
            print("Please enter a valid year. :( ")


def get_valid_rating():
    """Get a valid rating input from the user"""
    while True:
        try:
            rating = float(input("Enter movie rating (0-10): "))
            if 0 <= rating <= 10:
                return rating
            print("Please enter a rating between 0 and 10. eg: 4.2 OR 6.9  :( ")
        except ValueError:
            print("Please enter a valid rating. :( ")


def get_valid_title():
    """Get a valid title input from the user"""
    while True:
        title = input("Enter movie title: ").strip()
        if title:  # Check if title is not empty
            return title
        print("Title cannot be empty. :( ")


def list_all_movies():
    movies = storage.list_movies()
    if not movies:
        print("No movies found. :( ")
        return True
    for movie in movies.values():
        print(movie)
    return True


def add_new_movie():
    title = get_valid_title()
    year = get_valid_year()
    rating = get_valid_rating()

    storage.add_movie(title, year, rating)
    print(f"Movie '{title}' added successfully! :) ")
    return True


def delete_existing_movie():
    title = input("Enter movie title to delete: ")
    if storage.delete_movie(title):
        print(f"Movie '{title}' deleted successfully! :) ")
    else:
        print(f"Movie '{title}' not found. :( ")
    return True


def update_existing_movie():
    title = input("Enter movie title to update: ")
    if not storage.list_movies().get(title):
        print(f"Movie '{title}' not found. :( ")
        return True

    rating = get_valid_rating()
    if storage.update_movie(title, rating):
        print(f"Movie '{title}' updated successfully! :) ")
    return True


def show_stats():
    movies = storage.list_movies()
    if not movies:
        print("No movies found. :( ")
        return True

    # Get all ratings
    ratings = [movie.rating for movie in movies.values()]

    # Calculate average rating
    avg_rating = sum(ratings) / len(ratings)
    print(f"\nAverage rating: {avg_rating:.2f}")

    # Calculate median rating
    med_rating = median(ratings)
    print(f"Median rating: {med_rating:.2f}")

    # Find the best movie
    max_rating = max(ratings)
    best_movies = [
        movie for movie in movies.values()
        if movie.rating == max_rating
    ]
    print("\nBest movie(s):")
    for movie in best_movies:
        print(f"- {movie} O_o ")

    # Find the worst movie
    min_rating = min(ratings)
    worst_movies = [
        movie for movie in movies.values()
        if movie.rating == min_rating
    ]
    print("\nWorst movie(s):")
    for movie in worst_movies:
        print(f"- {movie} o_0 ")

    return True


def show_random_movie():
    movies = storage.list_movies()
    if not movies:
        print("No movies found. :( ")
        return True

    random_movie = random.choice(list(movies.values()))
    print("\nYour random movie is:")
    print(random_movie)
    return True


def search_movies():
    search_term = input("Enter search term: ").lower()
    movies = storage.list_movies()

    found_movies = [
        movie for movie in movies.values()
        if search_term in movie.title.lower()
    ]

    if found_movies:
        print("\nFound movies:")
        for movie in found_movies:
            print(movie)
    else:
        print("No movies found matching your search.")
    return True


def show_movies_by_rating():
    movies = storage.list_movies()
    if not movies:
        print("No movies found. :( ")
        return True

    sorted_movies = sorted(
        movies.values(),
        key=lambda x: x.rating,
        reverse=True
    )

    print("\nMovies sorted by rating (highest to lowest):")
    for movie in sorted_movies:
        print(movie)
    return True


def show_movies_by_year():
    movies = storage.list_movies()
    if not movies:
        print("No movies found. :(")
        return True

    sorted_movies = sorted(
        movies.values(),
        key=lambda x: x.year
    )

    print("\nMovies sorted by year (oldest to newest):")
    for movie in sorted_movies:
        print(movie)
    return True


def exit_program():
    print(" (: Goodbye! :) ")
    return False
