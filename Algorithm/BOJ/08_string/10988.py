word = input()
# if word == word[::-1]:
#     print(1)
# else:
#     print(0)


def palindrome_check(word):
    if len(word) < 2:
        return 1
    if word[0] == word[-1]:
        return palindrome_check(word[1:-1])
    else:
        return 0

print(palindrome_check(word))