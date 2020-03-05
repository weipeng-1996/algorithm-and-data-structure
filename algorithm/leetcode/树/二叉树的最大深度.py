# 104

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归O(n)


def maxDepth(root):
    if not root:
        return 0
    else:
        left_height = maxDepth(root.left)
        right_height = maxDepth(root.right)
        return max(left_height, right_height) + 1

# 迭代O(n)


def maxDepth1(root):
    if not root:
        return 0
    stack = [(1, root)]
    height = 0
    while stack:
        cur_height, root = stack.pop()
        if root:
            height = max(height, cur_height)
            stack.append((cur_height + 1, root.left))
            stack.append((cur_height + 1, root.right))
    return height


tree = TreeNode(5)
print(maxDepth1(tree))
