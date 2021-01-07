def can_be_palindrome(word):
    if len(word) % 2:
        cnt = 0
        for i in word:
            if word.count(i) % 2:
                cnt += 1
        if cnt == 1:
            return True
        else:
            return False
    else:
        for i in word:
            if word.count(i) % 2:
                return False
        return True

print(can_be_palindrome('aabb'))
print(can_be_palindrome('aaaaaaabc'))
print(can_be_palindrome('abbcabb'))
print(can_be_palindrome('zyyzzzzz'))