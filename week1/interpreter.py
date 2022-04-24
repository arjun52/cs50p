ok = input("expression:")
math = ok.split()
x = math[0]
y = str(math[1])
z = math[2]
if y == "+":
    w = float(int(x) + int(z))
    print(w)
elif y == "-":
    w = float(int(x) - int(z))
    print(w)
elif y == "*":
    w = float(int(x) * int(z))
    print(w)
elif y == "/":
    w = float(int(x) / int(z))
    print(w)
else:
    print("this shoulnt be printed")
