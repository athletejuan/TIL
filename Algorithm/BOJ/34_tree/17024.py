N = int(input())
edges = [list(map(int, input().split())) for _ in range(N-1)]
tree = [[] for _ in range(N)]
grass = 0
# tree, grass = {}, 2

for r,c in edges:
    r,c = r-1, c-1
    tree[r].append(c)
    tree[c].append(r)

for node in tree:
    link = len(node)+1
    if grass < link:
        grass = link

# for r,c in edges:
#     if tree.get(r):
#         tree[r] += 1
#     else:
#         tree[r] = 2
#     if grass < tree[r]:
#         grass = tree[r]
#     if tree.get(c):
#         tree[c] += 1
#     else:
#         tree[c] = 2
#     if grass < tree[c]:
#         grass = tree[c]

print(grass)