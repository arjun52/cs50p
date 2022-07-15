due = 50
while due > 0:
    print("Amount Due:" + str(due))
    insert = int(input("Insert Coin:"))
    if insert in [25,10,5]:
        due = due - insert
if due < 0:
    due = due *  (-1)
    print("Change due:" + str(due))
if due == 0:
    print("Amount Due:0")
