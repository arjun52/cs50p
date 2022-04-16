x = input("What is the answer to the Great Question of Life, the Universe and Everything?")
if x.strip() == "42":
    print("Yes")
elif x.lower().strip() == "forty-two":
    print("Yes")
elif x.lower().strip() == "forty two":
    print("Yes")
else:
    print("No")
