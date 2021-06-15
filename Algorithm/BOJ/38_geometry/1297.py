I,H,W = map(int, input().split())
height = ((I**2)*((H**2/(H**2+W**2))))**.5
print(int(height), int(height*(W/H)))