class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        n = len(s)
        curr = set()

        res = 0

        while r < n:
            #print(curr)
            while s[r] in curr:
                curr.remove(s[l])
                l += 1
            curr.add(s[r])
            r += 1
            res = max(res, len(curr))
        
        return res




        