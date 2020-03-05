
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 中序
class Solution:
    # 迭代
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [1]
        res = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root == 1:
                break
            res.append(root.val)
            root = root.right
        return res
    # 递归
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def inorder(root):
            return inorder(root.left) + [root.val] + inorder(root.right) 
            if root else []
        return inorder(root)


# 前序
class Solution:
    # 递归
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def preorder(root):
            return [root.val] + preorder(root.left) + preorder(root.right) if root else []
        return preorder(root)
    # 迭代
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            if root:
                output.append(root.val)
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)
        return output

# 后序


class Solution:
    # 递归
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def postorder(root):
            return postorder(root.left) + postorder(root.right) + [root.val] if root else []
        return postorder(root)
    
    # 迭代
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return output[::-1]
