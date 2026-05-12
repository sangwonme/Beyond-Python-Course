N = int(input())

# Make tree and count edge
tree = {}
edge_cnt = 0
for _ in range(N):
    n, l, r = map(int, input().split())
    node = {}
    node['left'] = l
    node['right'] = r
    tree[n] = node
    if l != -1:
        edge_cnt += 1
    if r != -1:
        edge_cnt += 1

# Count rightest edge num
right_edge_cnt = 0
current_node = 1
while current_node != -1:
    if tree[current_node]['right'] != -1:
        current_node = tree[current_node]['right']
        right_edge_cnt += 1
    else:
        break

print(edge_cnt*2 - right_edge_cnt)
