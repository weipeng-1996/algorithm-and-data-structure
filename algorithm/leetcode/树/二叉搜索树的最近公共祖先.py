# 235
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归 O(n) O(n)
def lowestCommonAncestor(root, p, q):
    parent_val = root.val

    p_val = p.val

    q_val = q.val

    if p_val < parent.val and q_val < parent_val:

        return lowestCommonAncestor(root.left, p, q)

    elif p_val > parent.val and q_val > parent_val:

        return lowestCommonAncestor(root.right,p , q)
    else:

        return root


# 迭代 O(n) O(1)

def lowestCommonAncestor1(root, p, q):
    p_val = p.val
    q_val = q.val
    node = root
    while node:
        parent_val = node.val
        if p_val < parent_val and q_val < parent_val:
            node = node.left
        elif p_val > parent_val and q_val > parent_val:
            node = node.right
        else:
            return node
