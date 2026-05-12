N = int(input())

tree = {}
for i in range(N):
    node_num, left, right = input().split()
    node = {}
    node['left'] = left
    node['right'] = right
    tree[node_num] = node

def preorder(node):
    if node != '.':
      print(node, end='')
      preorder(tree[node]['left'])
      preorder(tree[node]['right'])

def inorder(node):
    if node != '.':
      inorder(tree[node]['left'])
      print(node, end='')
      inorder(tree[node]['right'])

def postorder(node):
    if node != '.':
      postorder(tree[node]['left'])
      postorder(tree[node]['right'])
      print(node, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
