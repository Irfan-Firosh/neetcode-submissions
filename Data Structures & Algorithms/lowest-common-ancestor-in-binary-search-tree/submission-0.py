# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:



        def traverse(curr):
            a = min(p.val, q.val)
            b = max(p.val, q.val)
            if (a <= curr.val and curr.val <= b):
                return curr
            if b < curr.val:
                return traverse(curr.left)
            return traverse(curr.right)
        
        return traverse(root)
        