import os

def create_file(name, file_type="text"):
    ext = {
        "text": ".txt",
        "python": ".py",
        "html": ".html",
        "csv": ".csv"
    }
    filename = name + ext.get(file_type, ".txt")
    with open(filename, "w") as f:
        f.write("")
    return filename

def read_file(filename):
    if not os.path.exists(filename):
        return "File not found"

    with open(filename, "r") as f:
        return f.read()
