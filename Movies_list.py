import requests
import csv

file_path = "/Users/shreshthsingh/python_assignments/python_assignments/Hello.csv"
base_url = "http://www.omdbapi.com/"
api_key   = "6b7086e5"         

def get_response(title: str):
    """Return OMDb data for a single title, or None if not found."""
    params = {
        "t": title,
        "apikey": api_key
    }
    response = requests.get(url=base_url, params=params, timeout=10)
    
    if response.status_code != 200:
        print(f" error for '{title}")
        return None
    
    data = response.json()
    if data.get("Response") == "False":          
        print(f" Not found: {title}")
        return None
    
    print(f" Found: {title}")
    return data

def store_in_csv(rows: list, filepath: str):
    if not rows:
        print("Nothing to write")
        return
    
    fields_to_write = [
        "Title", "Year", "Rated", "Released",
        "Runtime", "Genre", "Director"
    ]
    
    with open(filepath, "w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(fields_to_write)          
        for data in rows:
            csv_writer.writerow(
                [data.get(field, "N/A") for field in fields_to_write]
            )
    
def getinput():
    titles_input = input("Enter movie / series titles (comma-separated): ")
    titles = [t.strip() for t in titles_input.split(",")]
    results = []
    for title in titles:
        movie_data = get_response(title)
        if movie_data:                
            results.append(movie_data)
    return results

result = getinput()
store_in_csv(result, file_path)