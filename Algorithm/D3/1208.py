for tc in range(1, 11):
    dump_times = int(input())
    boxes = list(map(int, input().split()))

    # 박스 높이의 분포를 카운팅하고, 이때 가장 높은 높이와 가장 낮은 높이를 찾는다.
    heights_num = [0] * 101
    max_height = 0
    min_height = 100
    for box in boxes:
        heights_num[box] += 1
        if max_height < box:
            max_height = box
        if min_height > box:
            min_height = box

    # 덤프를 실시한다. 가장 높은 높이와 가장 낮은 높이의 카운팅을 하나 차감해주고,
    # 가장 낮은 높이보다 하나 큰 높이와 가장 높은 높이보다  하나 작은 높이의 카운팅을 하나 높인다.
    for dump in range(dump_times):

        # 더이상 덤프를 못하는 경우 break문으로 빠져 나와준다.
        if max_height - min_height < 2:
            result = max_height - min_height
            break

        heights_num[max_height] -= 1
        heights_num[max_height - 1] += 1
        heights_num[min_height] -= 1
        heights_num[min_height + 1] += 1

        # 가장 높은 높이와 가장 낮은 높이를 업데이트 한다
        if not heights_num[max_height]:
            max_height -= 1
        if not heights_num[min_height]:
            min_height += 1

        result = max_height - min_height

    print('#{} {}'.format(tc, result))


# for tc in range(1, 11):
#     count = int(input())
#     boxes = list(map(int, input().split()))
#     for i in range(count):
#         max_idx = min_idx = 0
#         for idx, box in enumerate(boxes):
#             if not idx:
#                 max_val = min_val = box
#             else:
#                 if max_val < box:
#                     max_idx, max_val = idx, box
#                 if min_val > box:
#                     min_idx, min_val = idx, box
#         boxes[max_idx] -= 1
#         boxes[min_idx] += 1
#     for j in range(100):
#         if not j:
#             top = bottom = boxes[0]
#         else:
#             if boxes[j] > top:
#                 top = boxes[j] 
#             if boxes[j] < bottom:
#                 bottom = boxes[j] 
#     print('#{} {}'.format(tc, top - bottom))



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