n = int(input())
tri = []
tot = []

for i in range(n):
    temp = []
    tri.append(list(map(int, input().split())))
    if not i:
        tot.append(tri[0][0])
    else:
        for j in range(len(tot)):
            for k in range(2):
                path = tot[j] + tri[i][j+k]
                temp.append(path)
        if i > 1:
            re = []
            re.append(temp[0])
            for l in range(i-1):
                re.append(max(temp[(2*l)+1],temp[(2*l)+2]))
            re.append(temp[-1])
            temp = re 
        tot = temp
print(max(tot))