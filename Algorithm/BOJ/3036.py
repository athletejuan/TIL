N = input()
rings = list(map(int, input().split()))
first = rings[0]

for ring in rings[1:]:
    A = first
    B = ring
    while B:
        if A < B:
            A,B = B,A
        A,B = B,A-B
    print(f'{first//A}/{ring//A}')