import inflect
p = inflect.engine()
names = []
try:
    while True:
        ok = input("input:")
        names.append(ok)
except EOFError:
    print("\n")
    print("Adieu, adieu, to " + p.join(names))
