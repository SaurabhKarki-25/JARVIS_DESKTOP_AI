import webbrowser

def open_site(name):
    sites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com"
    }
    webbrowser.open(sites.get(name, "https://www.google.com"))

def search_google(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")
