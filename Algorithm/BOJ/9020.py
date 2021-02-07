T = int(input())

prime_num = []
for n in range(2, 10000):
    check = [0, 0] + [1]*(n-2)
    for idx, num in enumerate(check):
        if num: 
            if n%idx:
                for i in range(idx, n, idx):
                    check[i] = 0
            else:
                break
    else:
        prime_num.append(n)

for _ in range(T):
    even = int(input())
    gold = even//2
    start = 0
    if not gold%2 and even != 4:
        start = 1
    for j in range(start, gold, 2):
        if gold-j in prime_num and gold+j in prime_num:
            print(f'{gold-j} {gold+j}')
            break


# 함수 시간초과
# def prime(n):
#     check = [0, 0] + [1]*(n-2)
#     for idx, num in enumerate(check):
#         if num: 
#             if n%idx:
#                 for i in range(idx, n, idx):
#                     check[i] = 0
#             else:
#                 return False
#     return True

# for _ in range(T):
#     even = int(input())
#     gold = even//2
#     start = 0
#     if not gold%2 and even != 4:
#         start = 1
#     for j in range(start, gold, 2):
#         if prime(gold-j) in prime_num and prime(gold+j) in prime_num:
#             print(f'{gold-j} {gold+j}')
#             break