def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
def is_valid(s):
    if len(s) == 1:
        return False
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    if len(s) < 2 or len(s) > 6:
        return False
    for x in s:
        if x in [',','.',' ','!','?']:
            return False
    w = 0
    while w < len(s):
        if s[w].isalpha() == False:
            if s[w] == '0':
                return False
            else:
                break
        w += 1
    for q in range(len(s)):
        if s[q].isdigit():
            if not s[q:].isdigit():
                return False
    return True
main()
