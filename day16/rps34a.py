import random
options = ['rock', 'paper', 'scissors']
options_string = ', '.join(options)
outcomes = {
    'rock': {'rock': 'tie', 'paper': 'loss', 'scissors': 'win'},
    'paper': {'rock': 'win', 'paper': 'tie', 'scissors': 'loss'},
    'scissors': {'rock': 'loss', 'paper': 'win', 'scissors': 'tie'},
}
score = {'human': 0, 'computer': 0}
# return outcomes[human][computer]

def simple_player_choice():
    choice = input("Choose rock, paper, or scissors  ")
    return choice

def simple_player_choice_validation():
    choice = input("Choose rock, paper, or scissors  ")
    while choice != 'rock' and choice != 'paper' and choice != 'scissors':
        choice = input("Try again ")
    return choice

def get_player_choice():
    """Take player input, check to make sure it's a valid
    choice, and return the player's valid choice."""

    # The prompt uses option_string so it will update
    # if I change my set of options
    # The return value from input has .lower() called on it
    # to convert to lowercase before storing in choice
    choice = input(f"Choose an option from: {options_string} >> ").lower()

    # choice in options would return True if the choice were
    # contained in options, so this is the reverse!
    while choice not in options:
        choice = input(f"Bad human! Choose an option from: {options_string} >> ").lower()

    return choice

def get_computer_choice():
    """Return a random choice for the computer"""
    choice = random.choice(options)
    return choice

def get_outcome(human, computer):
    """Return win lose or tie, from the human's perspective"""
    return outcomes[human][computer]

def update_score(outcome):
    """Update the score to reflect the results of the round"""
    global score    # use this line to modify the global score
    if outcome == 'win':
        score['human'] += 1
    elif outcome == 'loss':
        score['computer'] += 1
    else:
        print("NOBODY WINS, YOU BOTH LOSE!")
    
    return

# while score['human'] <2 and score['computer'] < 2:
while True:
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    print(f"Human chose {player_choice} and computer chose {computer_choice}")
    outcome = get_outcome(player_choice, computer_choice)
    print(outcome)
    update_score(outcome)
    print(score)
    if score['human'] >= 2 or score['computer'] >= 2:
        break