T = int(input())

for test_case in range(1, T+1):
    word = input()
    fir = '..#.'
    sec = '.#'
    text = '#.'
    if len(word) == 1:
        print(f'{fir}'+'.')
        print(f'{sec}'*2+'.')
        print(f'{text}{word}{sec}')
        print(f'{sec}'*2+'.')
        print(f'{fir}'+'.')
    else:
        print(f'{fir}'*len(word)+'.')
        print(f'{sec}'*(len(word)*2)+'.')
        for i in word:
            text += i+f'{sec}'+'.'
        print(f'{text[:-1]}')
        print(f'{sec}'*(len(word)*2)+'.')
        print(f'{fir}'*len(word)+'.')