vowels = list(input("Input:"))
if 'A' in vowels:
    while 'A' in vowels:
        vowels.remove('A')
if 'a' in vowels:
    while 'a' in vowels:
        vowels.remove('a')
if 'E' in vowels:
    while 'E' in vowels:
        vowels.remove('E')
if 'e' in vowels:
    while 'e' in vowels:
        vowels.remove('e')
if 'I' in vowels:
    while 'I' in vowels:
        vowels.remove('I')
if 'i' in vowels:
    while 'i' in vowels:
        vowels.remove('i')
if 'O' in vowels:
    while 'O' in vowels:
        vowels.remove('O')
if 'o' in vowels:
    while 'o' in vowels:
        vowels.remove('o')
if 'U' in vowels:
    while 'U' in vowels:
        vowels.remove('U')
if 'u' in vowels:
    while 'u' in vowels:
        vowels.remove('u')
print(''.join(vowels))
