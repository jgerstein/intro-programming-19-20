import random

rounds = int(input("How many rounds do you want to play?  "))
options = ['rock', 'paper', 'scissors']
options_string = ', '.join(options)
outcomes = {
    'rock': {'rock': 'tie', 'paper': 'loss', 'scissors': 'win'},
    'paper': {'rock': 'win', 'paper': 'tie', 'scissors': 'loss'},
    'scissors': {'rock': 'loss', 'paper': 'win', 'scissors': 'tie'},
}
score = {'player': 0, 'computer': 0}

def get_player_choice():
    """Return a valid choice by the player for this round"""
    choice = input(f"Pick from the following: {options_string} --> ").lower()
    while choice not in options:
        choice = input(f"Bad human. Try again. Your valid options are: {options_string} --> ").lower()
    return choice

def get_computer_choice():
    """Return a random choice for this round"""
    choice = random.choice(options)
    return choice

def compare_choices(player, computer):
    """Compare choices of player and computer and 
    return win, loss, or tie from player's perspective"""
    return outcomes[player][computer]

def adjust_score(result):
    """Adjust scores based on result of this round"""
    global score
    if result == 'win':
        score['player'] += 1
    elif result == 'lose':
        score['computer'] += 1
    else:
        print("NOBODY WINS! You both failed at this")
    return


# Get choices from computer and player

# for round in range(rounds):
# while score['human'] < 2 and score['computer'] < 2:
while True:
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    print(f"Computer: {computer_choice}, Human: {player_choice}")
    result = compare_choices(player_choice, computer_choice)
    adjust_score(result)
    print(score)
    if score['human'] >= rounds or score['computer'] >= rounds:
        break
# worry about looping later