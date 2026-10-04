# Python Phone Book

A phone book app built in Python to practice core programming concepts in a new language. It started as a **terminal program** and grew into a small **Flask web app**. You can add, search, and delete contacts, and your contacts are saved to a file so they are still there after the app restarts.

## Features

- **Add** contacts with a name, phone number, and email
- **View** all saved contacts
- **Search** for a contact by name (case-insensitive, so "giselle" finds "Giselle")
- **Delete** a contact
- **Saves contacts to a JSON file** and loads them back when the app starts
- Two versions: a browser-based web app (`app.py`) and the original terminal menu (`terminal.py`)

## Technologies Used

- **Python 3**
- **Flask** (routes, forms, templates)
- **HTML and CSS** (Jinja templates, custom styling with Google Fonts)
- **JSON** for saving data
- **Git and GitHub**

## How to Run

**Web version**

1. Clone the repo
2. Install Flask: `pip3 install flask`
3. Start the server: `python3 app.py`
4. Open `http://localhost:5001` in your browser

The app uses **port 5001** because macOS uses port 5000 for AirPlay Receiver by default.

The first time you run the web version there is no `contacts.json` yet. The app handles that and starts with an empty phone book. The file is created when you add your first contact.

**Terminal version**

1. Run `python3 terminal.py`
2. Choose an option from the menu

## What I Learned

- Applying core concepts like **loops, variables, and functions** in a new language
- Using **dictionaries**, including nested dictionaries, for fast lookups
- Matching names without caring about capitalization, and trimming extra whitespace from search input
- How **Flask routes** work, including GET vs. POST, `request.form`, and redirects
- Passing data into HTML with **Jinja templates**, including loops and hidden form inputs
- **Saving and loading data with JSON**, and using `try`/`except` to handle a missing file
- **Debugging** real problems: route order, a port conflict with AirPlay, stale browser caches
- **Styling a page with CSS**: fonts, colors, borders, layout, and hover effects

## Future Improvements

- Support **multiple contacts with the same name** by giving each one a unique ID instead of using the name as the dictionary key
- **Search by phone number or email**
- Add an **edit** option for existing contacts
- Store contacts in a **database** instead of a JSON file
