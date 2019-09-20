answer = input("Choose a number")

try:
    answer = int(answer)
    print(f"{answer} * 100 = {answer * 100}")
except:
    print("That's not a number")
