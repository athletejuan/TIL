import sys
input = sys.stdin.readline

N,M = map(int, input().split())
poket = []
monster = []
for i in range(N):
    mon = input().rstrip()
    poket.append(mon)
    monster.append([mon, i+1])
monster.sort()

def check(num):
    if num[0] in '0123456789':
        return True
    else:
        return False

for j in range(M):
    target = input().rstrip()
    if check(target):
        print(poket[int(target)-1])
    else:
        L = 0
        R = N-1
        while L <= R:
            mid = (L+R)//2
            if monster[mid][0] == target:
                print(monster[mid][1])
                break
            elif monster[mid][0] < target:
                L = mid + 1
            else:
                R = mid - 1