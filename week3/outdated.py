months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
num = ['1','2','3','4','5','6','7','8','9','10','11','12']
dict = {"January" : 1,"February" : 2,"March" : 3,"April" : 4,"May" : 5,"June" : 6,"July" : 7,"August" : 8,"September" : 9,"October" : 10,"November" : 11,"December" : 12}
ok = input("input:")
if "," in ok: #input:September 8, 1636 = 1636-09-08
    comma = ok

    comma = comma.replace(",", "")
    comma = comma.split()
    if comma[0] in num or int(comma[1]) > 31:
        comma = input("input:")
    if comma[0] in months:
        print(str(comma[2]) + "-" + str(f"{int(dict[comma[0]]):02}") + "-" + str(f"{int(comma[1]):02}"))
if "/" in ok: #input: 9/8/1636 = 1636-09-08
    slash = ok
    slash = slash.replace("/", " ")
    slash = slash.split()
    for x in slash:
        if x in months:
            slash = input("input:")
    if int(slash[0]) > 12 or int(slash[1]) > 31:
        slash = input("input:")
    if slash[0] in num:
        print(str(slash[2]) + "-" + str(f"{int(slash[0]):02}") + "-" + str(f"{int(slash[1]):02}"))
for x in months:
    if x in ok and ',' not in ok:
        ok = input("input:")
    if x in ok and '/' in ok:
        ok = input("input:")

