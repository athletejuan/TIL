while True:
    n = int(input())
    if n < 0:
        break
    prime = []
    for i in range(1, n//2+1):
        if not n%i:
            prime.append(i)
    if sum(prime) == n:
        print('{} = {}'.format(n, ' + '.join(map(str, prime))))
    else:
        print('{} is NOT perfect.'.format(n))