diff = input("Pick easy, medium, or hard >> ").lower()

if diff == 'easy':
    x = 50
elif diff == 'medium':
    x = 20
elif diff == 'hard':
    x = 5
    
for n in range(x):
    print(n)