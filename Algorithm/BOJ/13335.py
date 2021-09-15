n,w,L = map(int, input().split())
trucks = list(map(int, input().split()))
bridge = [0]*w
time = i = 0

while i < n:
    weight = 0
    for j in range(w):
        weight += bridge[j]
    weight -= bridge.pop(0)
    if weight + trucks[i] > L:
        bridge.append(0)
    else:
        bridge.append(trucks[i])
        i += 1
    time += 1
print(time+w)