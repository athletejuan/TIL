for tc in range(1, 11):
    count = int(input())
    boxes = list(map(int, input().split()))
    for i in range(count):
        max_idx, min_idx = 0, 0
        for idx, box in enumerate(boxes):
            if not idx:
                max_val, min_val = box, box
            else:
                if max_val < box:
                    max_idx, max_val = idx, box
                if min_val > box:
                    min_idx, min_val = idx, box
        boxes[max_idx] -= 1
        boxes[min_idx] += 1
    for j in range(100):
        if not j:
            top, bottom = boxes[0], boxes[0]
        else:
            if boxes[j] > top:
                top = boxes[j] 
            if boxes[j] < bottom:
                bottom = boxes[j] 
    print('#{} {}'.format(tc, top - bottom))



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


# 1st try
# for tc in range(1, 11):
#     count = int(input())
#     boxes = sorted(list(map(int, input().split())))
#     for i in range(count):
#         boxes.extend([boxes.pop()-1, boxes.pop(0)+1])
#         boxes.sort()
#         gap = boxes[-1] - boxes[0]
#         if gap < 2:
#             print('#{} {}'.format(tc, gap))
#             break
#     else:
#         print('#{} {}'.format(tc, gap))