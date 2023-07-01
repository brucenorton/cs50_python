# use a library (library_sayings.py) to say hello and goodbye
#run from here with: python3 library_say.py Bruce
import sys
from library_sayings import hello, goodbye

if len(sys.argv) == 2:
  hello(sys.argv[1])
  goodbye(sys.argv[1])

