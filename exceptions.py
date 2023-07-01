#try... except... else... finally
#syntax errors
#runtime errors
#main() function 
#importing

##print ('hello world', __name__, __doc__, __package__)

#import dictionary ##why not put the .py??
#from mario import print_square

#from number.py hour 4:10
def main():
  # x = get_int()
  # print(f"x is {x}")

  # y = get_another()
  # print(f"y is {y}")

  z = get_third()
  print(f"z is {z}")
  
def get_int():
  try: 
    x = int(input("What's x? "))
  except ValueError:
    print("You must enter a number")
    return get_int() #need to recursively call the function
  else:
    return x #why does this return "None" A. see line 24

#another way with infinite loop
def get_another():
  while True:
    try:
      y = int(input("What's y? "))
      break
    except ValueError:
      print("You must enter an integer")
    else:
      break
  return y  

#tightened up and return directly
def get_third():
  while True:
    try:
      return int(input("What's z? "))
    except ValueError:
      pass #pass does nothing, but allows the loop to continue

if __name__ == "__main__":
    main()

#change