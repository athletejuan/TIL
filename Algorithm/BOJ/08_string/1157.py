word = input()
chars = word.upper()

many = {}
nums = []
most = []
for i in set(chars):    
    many[i] = chars.count(i)
    nums.append(chars.count(i))
for j in many:
    if many[j] == sorted(nums)[-1]:
        most.append(j)
if len(most) > 1:
    print('?')
else:
    print(most[0])