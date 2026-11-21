class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        n = len(s)
        last_seen = {}


        res = 0

        while r < n:
            #print(curr)
            if s[r] in last_seen:
                l = max(l, last_seen[s[r]] + 1)
            last_seen[s[r]] = r
            res = max(res, r - l + 1)
            r += 1
        
        return res




        