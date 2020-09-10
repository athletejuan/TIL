N = int(input())
aliquots = sorted(list(map(int, input().split())))
print(aliquots[0]*aliquots[-1])