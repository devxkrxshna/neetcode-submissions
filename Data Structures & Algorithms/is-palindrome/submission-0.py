class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_str= [c.lower() for c in s if c.isalnum()]
        fin_str="".join(cleaned_str)
        return fin_str==fin_str[::-1]

        