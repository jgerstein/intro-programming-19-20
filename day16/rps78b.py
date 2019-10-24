import random

wins_to_end = 2
options = ['rock', 'paper', 'scissors']
options_string = ', '.join(options)
score = {'player': 0, 'computer': 0}
outcomes = {
    'rock': {'rock': 'tie', 'paper': 'lose', 'scissors': 'win'},
    'paper': {'rock': 'win', 'paper': 'tie', 'scissors': 'lose'},
    'scissors': {'rock': 'lose', 'paper': 'win', 'scissors': 'tie'}
}

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
    """Choose a random item from our valid options.
    Return that random choice."""
    choice = random.choice(options)
    return choice


# Compare results

def get_outcome_long(player, computer):
    """Compare player's choice to computer's choice
    and determine whether the human had
    a win, a loss, or a tie"""

    # Print what the user and computer chose
    print(f"Player: {player}, Computer: {computer}")
    # Return win/loss/tie
    if player == 'rock':
        if computer == 'scissors':
            outcome = 'win'
        elif computer == 'paper':
            outcome = 'lose'
        else:
            outcome = 'tie'
    return outcome

def get_outcome(player, computer):
    """Return win, lose, or tie depending on the
    player and computer choices"""
    print(f"Player: {player}, Computer: {computer}")
    return outcomes[player][computer]

def update_score(outcome):
    """Figure out who gets the point, and add it to the 
    appropriate score"""
    global score
    if outcome == 'win':
        score['player'] += 1
    elif outcome == 'lose':
        score['computer'] += 1
    else:
        print("NO POINTS FOR EITHER OF YOU!")
    print(f"Updated score is: {score}")

def determine_overall_winner(score_dict):
    """Return the key for the winner of the game"""
    if score['player'] > score['computer']:
        return 'player'
    else:
        return 'computer'

def determine_overall_winner_2(score_dict):
    win_score = 0
    winner = ''
    for k, v in score.items():
        if v > win_score:
            winner = k
            win_score = v
    return winner

# while score['player'] < 2 and score['computer'] < 2:
while True:
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    result = get_outcome(player_choice, computer_choice)
    update_score(result)
    if score['player'] >= 2 or score['computer'] >= 2:
        break


print(f"The final scores are {score}")