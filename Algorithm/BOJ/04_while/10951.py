import sys

A,B = map(int, input().split())

while True:
    print(A+B)
    line = sys.stdin.readline().rsplit()
    if not line:
        break
    A,B = map(int, line)