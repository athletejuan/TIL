KMP = input()

short = ''
for i in KMP:
    if i.isupper():
        short += i
print(short)