class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def store(i , j):
            return (j-i) * min(heights[i], heights[j])
        
        # brute force is to check all pairs and compute
        n = len(heights)
        l = 0
        r = n - 1

        area = 0

        while l < r:
            area = max(area, store(l,r))

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return area


