class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]

        def bt(nums):
            if not nums:
                return [[]]
            

            left = nums[0]
            right = bt(nums[1:])
            ret = []

            for r in right:
                ret.append(r)
                ret.append([left] + r)
            return ret
        


        return bt(nums)


        