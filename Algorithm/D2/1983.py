T = int(input())

for test_case in range(1, T+1):
    nums = list(map(int, input().split()))
    result = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D']
    rank = []
    for i in range(nums[0]):
        score = list(map(int, input().split()))
        total = score[0]*.35 + score[1]*.45 + score[2]*.2
        rank.append(total)
    ranking = sorted(rank, reverse=True)
    print(f'#{test_case} {result[(ranking.index(rank[nums[1]-1]))//(int((nums[0])/10))]}')