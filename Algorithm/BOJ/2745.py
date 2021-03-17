N,B = input().split()
ex = 0

for num in range(len(N)):
    if int(B) > 10 and N[num].isalpha():
        ex += (ord(N[num])-55) * (int(B)**(len(N)-num-1))
    else:
        ex += int(N[num]) * (int(B)**(len(N)-num-1))
print(ex)