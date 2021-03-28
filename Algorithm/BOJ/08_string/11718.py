while True:
    try:
        text = input()
        if not text:
            break
        print(text)
    except EOFError:
        break