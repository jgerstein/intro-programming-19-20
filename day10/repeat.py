play_game = True

while active == True:

    secret = 5

    for turns in range(10, 0, -1):
        choice = int(input("pick a number: "))
        if choice == secret:
            print("you win")
            break
        if turns == 1:
            print("You lose")
            break
    
    if input("Play again?  ") == 'yes':
        active = True
    else:
        active = False

# print("why not?")