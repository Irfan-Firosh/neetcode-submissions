class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        valid = defaultdict(set)
        for i in range(n):
            for j in range(0, nums[i]+1):
                valid[i+j].add(i)
                valid[i+j].update(valid[i])
        
        #print(valid)
  
        return True if 0 in valid[n-1] else False

        