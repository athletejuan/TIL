T = int(input())

for _ in range(T):
    H,W,N = map(int, input().split())
    floor = N%H
    if not floor:
        floor = H
        room = N//H
    else: 
        room = N//H+1
    if room < 10:
        room = '0' + str(room)
    print(str(floor) + str(room))