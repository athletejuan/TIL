import sys
input = sys.stdin.readline

L = input()
text = input().rstrip()
hash_val = 0

for idx, char in enumerate(text):
    hash_val += (ord(char)-96)*(31**idx)
print(hash_val%1234567891)