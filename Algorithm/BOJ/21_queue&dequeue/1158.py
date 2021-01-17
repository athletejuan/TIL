N,K = map(int, input().split())
Jose = []
order = []
for i in range(N):
    Jose.append(str(i+1))

m = K-1
for _ in range(N):
    for idx, J in enumerate(Jose):
        if m < N:
            if idx == m:
                order.append(Jose.pop(idx))
                N -= 1
                m += (K-1)
        else:
            while m >= N:
                m -= N
if Jose:
    order += Jose
print(f'<{", ".join(order)}>')