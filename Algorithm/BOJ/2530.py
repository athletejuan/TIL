A,B,C = map(int, input().split())
D = int(input())

A += D//3600
B += D%3600//60
C += D%3600%60
if C >= 60:
    B += 1
if B >= 60:
    A += 1

print(f'{A%24} {B%60} {C%60}')