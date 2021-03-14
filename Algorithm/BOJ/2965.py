A,B,C = map(int, input().split())

jump = B-A
if C-B > jump:
    jump = C-B
print(jump-1)