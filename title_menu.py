import random

def print_title():
    title_text = r"""
   *        )     *       )        (       (      (                                       (        
 (  `    ( /(   (  `   ( /(        )\ )    )\ )   )\ )   (      *   )   (      (    (     )\ )     
 )\))(   )\())  )\))(  )\())(   ( (()/((  (()/(  (()/(   )\   ` )  /(   )\   ( )\   )\   (()/((    
((_)()\ ((_)\  ((_)()\((_)\ )\  )\ /(_))\  /(_))  /(_)|(((_)(  ( )(_)|(((_)( )((_|(((_)(  /(_))\   
(_()((_)_ ((_) (_()((_) ((_|(_)((_|_))((_)(_))   (_))_ )\ _ )\(_(_()) )\ _ )((_)_ )\ _ )\(_))((_)  
|  \/  \ \ / / |  \/  |/ _ \ \ / /|_ _| __/ __|   |   \(_)_\(_)_   _| (_)_\(_) _ )(_)_\(_) __| __| 
| |\/| |\ V /  | |\/| | (_) \ V /  | || _|\__ \   | |) |/ _ \   | |    / _ \ | _ \ / _ \ \__ \ _|  
|_|  |_| |_|   |_|  |_|\___/ \_/  |___|___|___/   |___//_/ \_\  |_|   /_/ \_\|___//_/ \_\|___/___|

"""

    # ANSI escape codes for colors
    red = "\033[38;5;196m"
    yellow = "\033[38;5;226m"
    orange = "\033[38;5;208m"
    reset = "\033[0m"

    colored_title = ""
    for char in title_text:
            color = random.choice([red, yellow, orange]) # Randomly choose color
            colored_title += color + char + reset

    print(colored_title)


def print_menu():
    menu_text = """
    Menu:
    0. Exit
    1. List movies
    2. Add movie
    3. Delete movie
    4. Update movie
    5. Stats
    6. Random movie
    7. Search movie
    8. Movies sorted by rating
    9. Movies sorted by year
    10. Generate Website

    Enter choice (1-10): 
    """
    print(menu_text)
