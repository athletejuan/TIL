for tc in range(1, 11):
    count = int(input())
    boxes = sorted(list(map(int, input().split())))
    for i in range(count):
        boxes.extend([boxes.pop()-1, boxes.pop(0)+1])
        boxes.sort()
        gap = boxes[-1] - boxes[0]
        if gap < 2:
            print('#{} {}'.format(tc, gap))
            break
    else:
        print('#{} {}'.format(tc, gap))


# mergeSort
# def mergeSort(x):
#     if len(x) > 1:
#         mid = len(x)//2
#         L,R = x[:mid],x[mid:]
#         mergeSort(L)
#         mergeSort(R)
    
#         Li, Ri, i = 0, 0, 0
#         while Li < len(L) and Ri < len(R):
#             if L[Li] < R[Ri]:
#                 x[i] = L[Li]
#                 Li += 1
#             else:
#                 x[i] = R[Ri]
#                 Ri += 1
#             i += 1
#         x[i:] = L[Li:] if len(L) != Li else R[Ri:]

# for tc in range(1, 11):
#     N = int(input())
#     boxes = list(map(int, input().split()))
#     mergeSort(boxes)

#     while N:
#         gap = boxes[-1] - boxes[0]
#         if gap < 2:
#             print('#{} {}'.format(tc, gap))
#             break
#         boxes[0] += 1
#         boxes[-1] -= 1
#         N -= 1
#         mergeSort(boxes)
#     else:
#         print('#{} {}'.format(tc, boxes[-1] - boxes[0]))