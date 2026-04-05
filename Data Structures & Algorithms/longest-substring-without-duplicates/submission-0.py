class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

            L = 0
            longest = 0
            sett = set()
            n = len(s)

            for R in range(n):
                while s[R] in sett:
                    sett.remove(s[L])
                    L += 1
                
                w = R - L + 1
                longest = max(longest, w)
                sett.add(s[R])
                
            return longest