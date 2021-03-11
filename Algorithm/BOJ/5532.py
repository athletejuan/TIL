L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

lang = A//C
math = B//D

if A%C:
    lang += 1
if B%D:
    math += 1
print(L - max(lang, math))