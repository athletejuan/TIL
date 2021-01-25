N = int(input())
numbers = list(map(int, input().split()))
count = 0

for num in numbers:
    if num == 1:
        pass
    else:
        check = [0, 0] + [1] * (num-1)
        for i in range(2, num):
            n = 1
            if check[i]:
                if not num % i:
                    break
                while i * n < num:
                    check[i * n] = 0
                    n += 1
        else:
            count += 1
print(count)