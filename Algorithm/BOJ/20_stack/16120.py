text = input()
stack = []
for char in text:
    stack.append(char)
    while stack[-4:] == ['P','P','A','P']:
        stack[-4:] = 'P'
print('PPAP' if stack == ['P'] else 'NP')