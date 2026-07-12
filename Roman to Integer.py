class Solution:
    def romanToInt(self, s: str) -> int:
        m =  {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        for c in range(len(s)):
            if c + 1 < len(s) and m[s[c]] < m[s[c+1]]:
                total -= m[s[c]]
            else :
                total += m[s[c]]
        return total
        
