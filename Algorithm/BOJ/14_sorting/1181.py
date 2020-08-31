N = int(input())

ws = set()
ml = 0
sw = []
for _ in range(N):
    ws.add(input())
words = sorted(list(ws))
for i in words:
    if len(i) > ml:
        ml = len(i)
for j in range(1, ml+1):
    for k in words:
        if len(k) == j:
            sw.append(k)
for word in sw:
    print(word)