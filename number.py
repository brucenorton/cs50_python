def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What's x? "))
            break
        except ValueError:
            print("You must enter a number")
        else:
            break
    return x  

if __name__ == "__main__":
    main()

#change
