x,y,w,h = map(int, input().split())

dis = [x, w-x, y, h-y]
print(min(dis))