import random
try:
    integer = int(input("level:"))
    if integer < 1:
        integer = int(input("level:"))
except ValueError:
    integer = int(input("level:"))

mystery = random.randint(1,integer)
x = 0
while x != mystery:
    x = input("guess:")
    try:
        if int(x) < int(mystery):
            print("Too small!")
        if int(x) > int(mystery):
            print("Too large!")
        if int(x) == int(mystery):
            print("Just right!")
            break
    except ValueError:
        x = input("guess:")
