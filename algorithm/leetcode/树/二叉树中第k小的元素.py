# 230

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(n) O(n)
def kthSmallest(root, k):
    stack = [root]
    arr = []
    while stack:
        temp = stack.pop()
        if temp:
            arr.append(temp.val)
            stack.append(temp.left)
            stack.append(temp.right)
    arr.sort()
    return arr[k-1]


# DFS 中序遍历 左根右 O(n) O(n)
def kthSmallest(root, k):
    def inorder(root):
        return inorder(root.left) + [root.val] + inorder(root.right) if r else []
    return inorder(root)[k]

# DFS 迭代 中序遍历 左根右 O(n) O(1)


def kthSmallest(root, k):
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            return temp.val
        root = root.right

