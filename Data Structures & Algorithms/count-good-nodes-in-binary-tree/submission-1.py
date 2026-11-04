# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        ret = 0

        def traverse(curr, compare):
            nonlocal ret
            if curr is None:
                return
            compare = max(compare, curr.val)
            if curr.val >= compare:
                ret += 1
            
            traverse(curr.left, compare)
            traverse(curr.right, compare)

            return
        
        traverse(root, root.val)
        return ret