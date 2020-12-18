N,M = map(int, input().split())

bundle = []
each = []
for _ in range(M):
    a,b = map(int, input().split())
    bundle.append(a)
    each.append(b)

print(min(min(bundle)*(N//6 + 1), min(bundle)*(N//6) + min(each)*(N%6), min(each)*N))