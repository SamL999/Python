import json 
import requests

url = "https://www.googleapis.com/books/v1/volumes?maxResults=5&q=Python&Projection=lite"
jsonfile = "books.json"
r = requests.get(url)
r.encoding = 'utf-8'

json_data = json.loads(r.text)

with open (jsonfile, "w") as fp :
    json.dump(json_data, fp)


