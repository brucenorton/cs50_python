#creates a library to be run with library_say.py
def hello(name):
    print(f"Hello {name}!")

def goodbye(name):
    print(f"Goodbye {name}!")

def main():
    hello("Fred")
    goodbye("Fred")

# __name__ is a special variable that is set for the file that is being run
if __name__ == "__main__":
    main()