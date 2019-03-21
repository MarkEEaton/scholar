import requests
import json
from pprint import pprint

baseurl = "https://doaj.org/api/v1/search/articles/"

abstracts = []

for page in range(67):
    data = requests.get(baseurl + "suggest?pageSize=100&sort=desc&page=" + str(page))
    print(data.status_code)
    try:
        results = data.json()["results"]
    except KeyError:
        print("breaking...")
        break
    for result in results:
        try:
            abstracts.append(result["bibjson"]["abstract"])
        except KeyError:
            pass
    print("page: " + str(page))

print(len(abstracts))
with open("data.json", "w") as f1:
    f1.write(json.dumps(abstracts))
