num_list = [1]*10000
self_num = []
s = 1

def self_check(n):
    m = n
    if num_list[n]:
        self_num.append(m)
        while n < 10000:
            while n:
                m += n%10
                n //= 10
            if m < 10000:
                num_list[m] = 0
            n = m

while s < 10000:
    if num_list[s]:
        self_check(s)
    s += 1
    
for num in self_num:
    print(num)