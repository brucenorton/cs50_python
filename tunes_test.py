#unit testing
# pip install pytest
# pytest tunes_test.py ...to run test

from tunes import get_tunes

def main():
  test_tunes()

bands = ["weezer", "beatles", "rolling stones"]

def test_tunes():
  for band in bands:
    results = get_tunes(band)
    for result in results["results"]:
      print(result["artistName"] + " - " + result["trackName"] + " - " + result["collectionName"])

if __name__ == "__main__":
    main()