import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit(1)

response = requests.get("https://itunes.apple.com/search?entity=song&limit=9&term=" + sys.argv[1])
## print(json.dumps(response.json(),indent=2))
o = response.json()
for result in o["results"]:
    print(result["artistName"] + " - " + result["trackName"] + " - " + result["collectionName"])
    # print(json.dumps(result,indent=
#change
# "artistName": "The Beatles",
# "collectionName": "The Beatles 1967-1970 (The Blue Album)",
# "trackName": "Hey Jude",