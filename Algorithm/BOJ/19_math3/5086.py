A,B = map(int, input().split())

def multi(A,B):
    if not A%B:
        return 'multiple'
    elif not B%A:
        return 'factor'
    else:
        return 'neither'

while A:
    print(multi(A,B))
    A,B = map(int, input().split())