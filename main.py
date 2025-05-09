import title_menu as t
import movie_functions as movie

COMMANDS = {
    "0": ("Exit", movie.exit_program),
    "1": ("List movies", movie.list_all_movies),
    "2": ("Add movie", movie.add_new_movie),
    "3": ("Delete movie", movie.delete_existing_movie),
    "4": ("Update movie", movie.update_existing_movie),
    "5": ("Stats", movie.show_stats),
    "6": ("Random movie", movie.show_random_movie),
    "7": ("Search movie", movie.search_movies),
    "8": ("Movies sorted by rating", movie.show_movies_by_rating),
    "9": ("Movies sorted by year", movie.show_movies_by_year)
}

def handle_command(choice):
    command = COMMANDS.get(choice)
    if command:
        return command[1]()
    print("Invalid choice, please try again.")
    return True

def main():
    t.print_title()
    running = True
    while running:
        t.print_menu()
        choice = input("Enter choice: ")
        running = handle_command(choice)

if __name__ == "__main__":
    main()
