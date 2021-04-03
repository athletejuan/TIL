cnt = 1
while True:
    L,P,V = map(int, input().split())
    if not L:
        break
    camping = (V//P)*L
    camping += L if V%P > L else V%P
    print('Case {}: {}'.format(cnt, camping))
    cnt += 1