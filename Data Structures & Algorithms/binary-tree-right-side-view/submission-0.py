# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # can just construct a level traversal and print all nodes that appear on the right
        if root is None:
            return []
        

        q = deque([root])
        ret = []

        while q:
            curr = None

            for _ in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            
            ret.append(curr.val)
        
        return ret

        