TC = int(input())

for tc in range(1, TC+1):
    S = input()
    K,i = 1,0
    last = S[i]
    while i < len(S)-1:
        if len(last) < 2:
            if last != S[i+1]:
                last = S[i+1]
                i += 1
            else:
                last = S[i+1:i+3]
                i += 2
        else:
            last = S[i+1]
            i += 1
        K += 1
    print('#{} {}'.format(tc, K-(i-len(S)+1)))