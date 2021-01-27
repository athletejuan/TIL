while True:
    text = input()
    re_text = ''
    if text == 'END':
        break
    for char in text:
        re_text = char + re_text
    print(re_text)