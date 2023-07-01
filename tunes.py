import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit(1)

response = requests.get("https://itunes.apple.com/search?entity=song&limit=9&term=" + sys.argv[1])
## print(json.dumps(response.json(),indent=2))
results = response.json()
for result in results["results"]:
    print(result["artistName"] + " - " + result["trackName"] + " - " + result["collectionName"])
