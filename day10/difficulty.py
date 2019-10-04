diff = input("Pick easy, medium, or hard >> ").lower()

if diff == 'easy':
    turns = 15
elif diff == 'medium':
    turns = 8
elif diff == 'hard':
    turns = 5

for n in range(turns):
    # play game
    print(n)