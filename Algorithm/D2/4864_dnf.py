T = int(input())

for test_case in range(1, T+1):
    str1 = input()
    str2 = input()
    for i in range(len(str2)-len(str1)+1):
        if str2[i:i+len(str1)] == str1:
            print(f'#{test_case} 1')
            break
    else:
        print(f'#{test_case} 0')


# Boyer-Moore Algorithm (미완??)
for test_case in range(1, T+1):
    str1 = input()
    str2 = input()

    s = str1[::-1]
    i = len(str1)-1
    result = 0

    while i < len(str2):
        nxt = len(s)
        j = 0
        if s[j] == str2[i]:
            while j < len(s):
                if s[j] != str2[i-j]:
                    break
                j += 1
            if j == len(s):
                result = 1
        else:
            while j < len(s):
                if s[j] == str2[i]:
                    nxt = min(j, nxt)
                    break
                j += 1
        if result:
            break
        i += nxt
    print(f'#{test_case} {result}')