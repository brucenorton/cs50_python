import json
import requests
import sys

if len(sys.argv) == 2:
    group = sys.argv[1]


def main():
    results = get_tunes(group)
    for result in results["results"]:
        print(result["artistName"] + " - " + result["trackName"] + " - " + result["collectionName"])


def get_tunes(group):
    response = requests.get("https://itunes.apple.com/search?entity=song&limit=3&term=" + group)
    ## print(json.dumps(response.json(),indent=2))
    return response.json()

if __name__ == "__main__":
    main()