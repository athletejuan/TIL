T = int(input())

for t in range(T):
    string = input()
    binary = []
    while len(string) > 1:
        binary.append(string[:2])
        string = string[2:]
    print(''.join(sorted(binary)))