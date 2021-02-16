T = int(input())

for tc in range(1, T+1):
    P,Pa,Pb = map(int, input().split())
    A,B = 0,0
    L,R = 1,P
    while L <= R:
        mid = (L+R)//2
        A += 1
        if mid == Pa:
            break
        elif mid > Pa:
            R = mid-1
        else:
            L = mid+1
    L,R = 1,P
    while L <= R:
        mid = (L+R)//2
        B += 1
        if mid == Pb:
            if A < B:
                print(f'#{tc} A')
                break
            elif A > B:
                print(f'#{tc} B')
                break
            else:
                print(f'#{tc} 0')
                break
        elif mid > Pb:
            R = mid-1
        else:
            L = mid+1


# Tony
# import sys
# sys.stdin = open('input.txt', 'r')


# def binary_search(left, right, target_page, count):
#     middle = int((left+right)/2)

#     if target_page < middle:
#         return binary_search(left, middle, target_page, count+1)
#     elif target_page > middle:
#         return binary_search(middle, right, target_page, count+1)
#     else:
#         return count


# T = int(input())

# for t in range(1, T+1):
#     total_page, target_a, target_b = map(int, input().split())
#     count_a = binary_search(1, total_page, target_a, 0)
#     count_b = binary_search(1, total_page, target_b, 0)

#     if count_a > count_b:
#         result = 'B'
#     elif count_a < count_b:
#         result = 'A'
#     else:
#         result = 0

#     print('#{} {}'.format(t, result))