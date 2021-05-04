S = input()
change = 0

for i in range(len(S)-1):
    if S[i] != S[i+1]:
        change += 1
        
if change%2:
    print(change//2+1)
else:
    print(change//2)