V = input()
votes = input()
A,B = 0,0

for i in votes:
    if i == 'A':
        A += 1
    else:
        B += 1

if A > B:
    print('A')
elif A < B:
    print('B')
else:
    print('Tie')