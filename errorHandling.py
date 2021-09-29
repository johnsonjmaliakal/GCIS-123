#PS1
def crazy_output():
  x = input("Type something: ")
  try:
    int_x = int(x)
    print("You entered an integer:",
      int_x)
  except ValueError:
    try:
      float_x = float(x)
      print("You entered a float:",
        float_x)
    except:
      print("The third character is:",
        x[2])

#crazy_output()

#PS2
def print_sequence(x):
    try:
        for i in x:
            print (i, end = ' ')
        print()
    except TypeError as te:
        print ("Not a sequence:", x)

#print_sequence(range(0, 20))
#print_sequence(20)

#PS3
def checker(x, y):
    if y > 10 or y < 1: #if input is out of range
        raise ValueError
    elif x == y:
        return True
    else:
        return False

def PS3():
    import random
    x = random.randint(1, 10)
    c = 3
    while c > 0:
        try:
            y = int(input("Guess a number between 1 and 10: "))
            if checker(x, y):
                print ("Correct! You guessed right,", x, "was the right answer!" )
                break
            else:
                c -= 1
                print("Wrong! You have", c, " guesses left.")
                continue
        except: #if input is not an integer
            raise ValueError
        
    else: #if user fails to guess after 3 chances
        raise ValueError

#PS3()

#PS4
def open_file():
    while True:
        file = input("Enter filename: ")
        try:
            with open (file, 'r') as x:
                for i in x:
                    print (i)
            break
        except:
            print ("File does not exist. Try again.")
            continue

#open_file()

#PS5
def print_chars(x):
    try:
        c = 0
        while True:
            a = x[c]
            print (a)
            c += 1
    except IndexError:
        return (c+1)

print(print_chars("abc"))
