def main():
    print_square(3)

def print_square(size):
    print("#" * size)
    for i in range(size):
      print("#", end="")
    print()# prints a new line
    #add another row by calling a function
    print_row(size)

def print_row(width):
    print("#" * width)

main()
#changess
