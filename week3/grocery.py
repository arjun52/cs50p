dict = {}
while True:
    try:
        item = input().upper()
        if item in dict:
            dict[item] += 1
        else:
            dict[item] = 1



    except EOFError:
        print("\n")
        for x in sorted(dict.keys()):
            print(dict[x], x )
        break
