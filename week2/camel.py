userinput = input("camelcase input:")
for c in userinput:
    if c.isupper():
        print("_"+c.lower(), end="")
    else:
        print(c, end="")
print()
