class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        max_len=0
        r=0
        hmap={}
        while r<len(s):
            if s[r] in hmap:
                l=max(hmap[s[r]]+1,l)
                
            hmap[s[r]]=r
            max_len = max(max_len,r-l+1)
            r+=1
        return max_len

       
            

        