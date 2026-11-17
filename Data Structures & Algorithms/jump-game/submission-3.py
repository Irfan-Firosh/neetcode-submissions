class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        i = n - 2
        goal = n-1
        while i > -1:
            print(goal, i)
            if goal == 0:
                return True
            if goal <= i + nums[i]:
                goal = i
            
            i -= 1

        return True if 0 + nums[0] >= goal else False

        