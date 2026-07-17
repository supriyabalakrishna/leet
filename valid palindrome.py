class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ""
        for c in s:
            if c.isalnum():
                t+=c.lower()
        if t == t[::-1]:
            return True
        else:
            return False
