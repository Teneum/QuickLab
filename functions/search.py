import requests
API_KEY = "KEY"
SEARCH_ENGINE_ID = "ID"


page = 1
start = (page - 1) * 10 + 1

def search(query):
    results = []
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"
    data = requests.get(url).json()
    search_items = data.get('items')
    for searches in search_items:
        details = {
            'Title': searches['title'],
            'Link': searches['link']
        }
        results.append(details)
    return results

