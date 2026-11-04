# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []

        def traverse(curr, level):
            nonlocal ret
            if curr is None:
                return
            if len(ret) < level+1:
                ret.append([curr.val])
            else:
                ret[level].append(curr.val)
            traverse(curr.left, level+1)
            traverse(curr.right, level+1)
        
        traverse(root, 0)
        return ret

        