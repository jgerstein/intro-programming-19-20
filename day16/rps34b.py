import random
wins_to_end = 2
options = ['rock', 'paper', 'scissors']
results = {
    'rock': {'rock': 'tie', 'paper': 'lose', 'scissors': 'win'},
    'paper': {'rock': 'win', 'paper': 'tie', 'scissors': 'lose'},
    'scissors': {'rock': 'lose', 'paper': 'win', 'scissors': 'tie'}
}
options_string = ', '.join(options)
scores = {'human': 0, 'computer': 0}

# Start with getting user's choice

def simple_choice():
    """Problems:
    * Won't recognize changing options
    * Won't check wrong capitalization
    * Really ugly conditional statement"""

    choice = input("Choose rock, paper, or scissors")
    while choice != 'rock' and choice != 'paper' and choice != 'scissors':
        choice = input("Try again")
    return choice

def get_user_choice():
    """Get and return a valid user choice"""
    choice = input(f"Choose from one of the following: {options_string} >> ").lower()
    
    # While choice isn't a valid choice, make them do it again!
    while choice not in options:
        choice = input(f"Bad human! Choose from one of the following: {options_string} >> ").lower()
    return choice

# Get computer's choice
def get_computer_choice():
    """Return a random valid choice"""
    return random.choice(options)


def get_outcome(user, computer):
    """Return the outcome of the match (win, lose, tie)
    Outcome is 'win', 'tie', or 'lose'"""
    # print selections
    print(f"User chose {user_selection} and computer chose {computer_selection}")

    # Use dictionary to get results of matchup
    outcome = results[user_selection][computer_selection]
    return outcome

while scores['human'] <= 2 and scores['computer'] <= 2:
    user_selection = get_user_choice()   # User chooses a valid option
    computer_selection = get_computer_choice()

    outcome = get_outcome(user_selection, computer_selection)

    if outcome == 'win':
        scores['human'] += 1
    elif outcome == 'lose':
        scores['computer'] += 1
    else:
        print("NO POINTS FOR EITHER OF YOU!")

    print(scores)
