def main():
    input1 = input()
    convertedinput = convert(input1)
    print(convertedinput)
def convert(input1):
    first = input1.replace(":)",'🙂')
    last = first.replace(":(",'🙁')
    return last
main()
