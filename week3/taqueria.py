dict = {
    "baja taco": 4.00,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}
price = 0
try:
    for x in range(1000):
        item = input("item:").lower()
        if item in dict:
            s = dict.get(item)
            price = round(price + s, 2)
            print("$" + str("{:.2f}".format(price)))
except EOFError:
    print("\n" "Total: $" + str("{:.2f}".format(price)))
