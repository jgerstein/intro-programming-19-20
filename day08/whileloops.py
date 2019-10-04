name = input("Who are you? ")

while name.lower() != "karen":
    name = input("You're not the person I wanted to talk to. ")

print(f"Hello {name}")