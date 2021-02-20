n = int(input())

def fibo(a,b):
    for _ in range(n-1):
        a,b = b,a+b
    return b

print(fibo(1,1)%10007)