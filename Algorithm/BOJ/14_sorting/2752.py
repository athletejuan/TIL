import sys
input = sys.stdin.readline

three = list(map(int,input().split()))
for i in range(2):
    for j in range(2-i):
        if three[j] > three[j+1]:
            three[j],three[j+1] = three[j+1],three[j]
print(' '.join(map(str, three)))