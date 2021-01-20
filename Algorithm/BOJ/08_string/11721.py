word = input()
split = len(word) // 10

for i in range(split+1):
    print(word[i*10:(i+1)*10])