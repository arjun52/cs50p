thing = input("greetings!")
input = thing.lower()
input = input.replace(",", "")
sentence = input.split()
wordlist = sentence[0]
if sentence[0] == "hello":
    print("$0")
elif wordlist[0] == "h":
    print("$20")
else:
    print("$100")
