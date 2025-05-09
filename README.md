# 🎬 Movie Project OOP Web

A Python command-line and web app to manage your personal movie collection!
Easily add, update, delete, rate, and view your movies-complete with poster images and a fiery ASCII art title.

---

## 🚀 Features

- **Beautiful ASCII Art Title:** Fiery, colorful welcome every time you launch!
- **Add Movies by Title:** Fetches details (year, rating, poster) from the OMDb API.
- **List All Movies:** View all your movies with year, rating, and poster info.
- **Update Ratings:** Change the rating for any movie.
- **Delete Movies:** Remove movies you no longer want.
- **Statistics:** See average, median, best, and worst ratings.
- **Random Movie:** Get a random movie suggestion from your collection.
- **Search:** Find movies by title (partial matches supported).
- **Sort:** View movies sorted by rating or by year.
- **Website Generation:** Instantly generate a stylish HTML page of your collection.

---

## 🗂️ Storage Options

Choose your preferred storage backend:

- **JSON** (`movies.json`)
- **CSV** (`movies.csv`)

Switch easily by changing a single line in `main.py`.

---

## 🛠️ Project Structure

    .
    ├── main.py             # Main entry point
    ├── movie_app.py        # Core app logic (menu, commands)
    ├── istorage.py         # Storage interface (abstract base class)
    ├── storage_json.py     # JSON file storage implementation
    ├── storage_csv.py      # CSV file storage implementation
    ├── title_menu.py       # ASCII art title and menu display
    ├── movies.json         # Example JSON movie data
    ├── movies.csv          # Example CSV movie data
    ├── _static/
    │   ├── index_template.html  # HTML template for website generation
    │   └── index.html           # Generated movie website
    └── README.md
    
---

## ⚡ Quickstart

1. **Install dependencies:**

```
pip install requests python-dotenv
```

2. **Set your OMDb API key:**
    - Get a free API key from [OMDb](https://www.omdbapi.com/apikey.aspx).
    - Create a `.env` file in your project directory:

```
OMDB_API_KEY=your_api_key_here
```

3. **Run the app:**

```
python main.py
```

4. **Follow the menu prompts to manage your movies!**

---

## 🌟 Example Usage

    * ) * ) ( ( ( (
    ( ` ( /( ( ` ( /( )\ ) )\ ) )\ ) ( * ) ( ( ( )\ )
    ... (fiery ASCII art) ...
    Menu:
    1. List movies
    2. Add movie
    ...
    Enter choice (1-10):
    
---

## 🖥️ Generate Your Movie Website

- Choose option `10` in the menu to generate a stylish HTML page of your collection.
- The site is created at `_static/index.html` and includes posters, ratings, and a fiery header!

---

## 💾 Switching Storage Backends

In `main.py`, comment/uncomment the desired storage:

    # JSON storage
    json_storage = StorageJson('movies.json')
    json_app = MovieApp(json_storage)
    
    # CSV storage
    # csv_storage = StorageCsv('movies.csv')
    # csv_app = MovieApp(csv_storage)
    
---

## 📦 Extending the Project

- Add new storage backends by implementing the `IStorage` interface.
- Customize the website template in `_static/index_template.html`.
- Style the HTML/CSS for your own fiery look!

---

## 📝 Credits

- ASCII art and color: `title_menu.py`
- OMDb API for movie data
- Developed with ❤️ and 🔥

---

## 📜 License

MIT License (or your preferred license)
