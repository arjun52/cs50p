try:
    dash = input("fraction:")
    useless = dash.replace('/',' ')
    frac = useless.split()
    one = int(frac[0])
    two = int(frac[1])
    perc = round(100 * (one/two))
    if perc >= 99 and perc <= 100:
        print("F")
    if perc <= 1 and perc >= 0:
        print("E")
    while perc > 100:
        dash = input("fraction:")
        useless = dash.replace('/',' ')
        frac = useless.split()
        one = int(frac[0])
        two = int(frac[1])
        perc = round(100 * (one/two))
    if perc < 99 and perc > 1:
        print(str(perc) + "%")
except (ValueError, ZeroDivisionError,):
    dash = input("fraction:")
    useless = dash.replace('/',' ')
    frac = useless.split()
    one = int(frac[0])
    two = int(frac[1])
    perc = round(100 * (one/two))
    if perc >= 99 and perc <= 100:
        print("F")
    if perc <= 1 and perc >= 0:
        print("E")
    elif perc < 99 and perc > 1:
        print(str(perc) + "%")
