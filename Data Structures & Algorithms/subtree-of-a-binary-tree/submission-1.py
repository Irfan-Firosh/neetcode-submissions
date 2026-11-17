# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def cmp(r, s):
            if r is None or s is None:
                if r is None and s is None:
                    return True
                return False
            
            if r.val == s.val:
                return cmp(r.left, s.left) and cmp(r.right, s.right)
            
            return False

        q = deque()
        q.append(root)

        arr = []

        while q:
            curr = q.popleft()
            if curr.val == subRoot.val:
                arr.append(curr)
            if curr.left is not None:
                q.append(curr.left)
            if curr.right is not None:
                q.append(curr.right)
        res = False
        for curr in arr:
            res = res or cmp(curr, subRoot)
        return res

            

        