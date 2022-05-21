def main():
    ok = input("time?")
    time = convert(ok)
    if time <= 8 and time >= 7:
        print("breakfast time")
    elif time <= 13 and time >= 12:
        print("lunch time")
    elif time <=19 and time >= 18:
        print("dinner time")
def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(float(minutes) / 60)

main()
