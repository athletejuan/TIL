wu = []
ku = []
wk = []
for _ in range(10):
    score = int(input())
    wu.append(score)

    for w in range(len(wu)-2, -1, -1):
        if wu[w] < score:
            wu[w+1] = wu[w]
            wu[w] = score

for _ in range(10):
    score = int(input())
    ku.append(score)

    for k in range(len(ku)-2, -1, -1):
        if ku[k] < score:
            ku[k+1] = ku[k]
            ku[k] = score
            
wk.append(sum(wu[:3]))
wk.append(sum(ku[:3]))

print(' '.join(map(str, wk)))