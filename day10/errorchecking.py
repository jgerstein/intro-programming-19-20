num = ""

# while we haven't chosen a number, repeat
while num == "":
    try:
        # try to do something
        num = int(input("Pick a number >>> "))
    except ValueError:
        # do something
        print("Do you not know what a number is?")

# this print statement represents the rest of the turn
print(num)