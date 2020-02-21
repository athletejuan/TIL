T = int(input())

for test_case in range(1, T+1):
    num = int(input())
    text = input().split()
    sent = []
    abc = []
    for idx, word in enumerate(text):
        if word[-1] == '.' or word[-1] == '!' or word[-1] == '?':
            word = word[:-1]
            abc.append(word)
            sent.append(idx)
        else:
            abc.append(word)
    trans = []
    for i in range(num):
        count = 0
        if not i:
            for j in abc[:((sent[i])+1)]:
                if j.isalpha():
                    if j.istitle():
                        count += 1
        else:
            for k in abc[(sent[i-1]+1):(sent[i]+1)]:
                if k.isalpha():
                    if k.istitle():
                        count += 1
        trans.append(str(count))
    print(f'#{test_case} {" ".join(trans)}')